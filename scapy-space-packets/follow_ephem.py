#!/usr/bin/env python3
"""Follow the position of the satellite using EPHEM packets

Dependencies:

    pip install --upgrade setuptools wheel
    pip install scapy numpy skyfield

Usage, with packets from Cosmos Preidentified router

    socat TCP:127.0.0.1:7779 - | ./follow_ephem.py

or

    ./follow_ephem.py -c 127.0.0.1:7779
"""
import argparse
import datetime
from skyfield.api import EarthSatellite, load
from skyfield.sgp4lib import TEME_to_ITRF
from skyfield.positionlib import ITRF_to_GCRS2
from numpy import array
import re
import os.path
import socket
import sys

from all_packets import pump_cosmos_ccsds_packets, EPHEM_EPHEM_PKT_TlmPkt  # noqa


# TLE from /cf/tle.txt
TLE = (
    '1 45446U 20020Y   20175.91667824 -.00053643  00000-0 -55554-2 0  9994',
    '2 45446  87.5774 107.8706 0026529 318.8145  47.7382 14.90176969 14161',
)
ts = load.timescale()
satellite = EarthSatellite(TLE[0], TLE[1], 'Hack-A-Sat', ts)


def TEME_to_GCRS(time, pos, vel):
    """Convert a position and velocity from TEME to GCRS coordinates, via ITRF

    * TEME: True Equator, Mean Equinox (used in TLE format and in SGP4 theory)
    * ITRF: International Terrestrial Reference Frame
    * GCRS: Geocentric Celestial Reference System (returned by method satellite.at)
    """
    pos, vel = TEME_to_ITRF(time.whole, pos, vel, 0.0, 0.0, time.ut1_fraction)
    return ITRF_to_GCRS2(time, pos, vel)


def check_ephem(e_pkt: EPHEM_EPHEM_PKT_TlmPkt):
    """Check the values from a received Ephemeris packet"""
    e_time_str = e_pkt.TIME_STRING.decode('ascii').rstrip('\0')
    assert e_time_str[-4] == '.', f"Unexpected ephem time {e_time_str!r}"  # time is in milliseconds
    e_time_str += '000'  # now, it is in microseconds, for %f format
    e_datetime = datetime.datetime.strptime(e_time_str, '%Y-%m-%d-%H:%M:%S.%f')

    e_abs_time_epoch = e_pkt.ABSOLUTE_TIME_EPOCH
    e_abs_time = e_pkt.ABSOLUTE_TIME
    e_abs_time_diff = e_abs_time - e_abs_time_epoch
    e_px = e_pkt.PosN_X
    e_py = e_pkt.PosN_Y
    e_pz = e_pkt.PosN_Z
    e_vx = e_pkt.VelN_X
    e_vy = e_pkt.VelN_Y
    e_vz = e_pkt.VelN_Z

    print(f"   EPHEM abs time: epoch {e_abs_time_epoch} + {e_abs_time_diff}")
    print(f"   EPHEM time: {e_datetime}")

    # Convert ABSOLUTE_TIME to a date
    # Julian date is the reference in astronomy, days start at noon (12:00).
    # Because of leap seconds, currently there is a 37s difference between
    # Terrestrial Time (TT) and International Atomic Time (TAI).
    e_abs_ts_time = ts.tai(2000, 1, 1, 12, 0, 37 + e_abs_time)
    # single-digit seconds are reprensented without a leading zero
    e_abs_ts_time_seconds = e_abs_ts_time.utc_strftime('%S')
    if e_abs_ts_time_seconds[0] == '0':
        e_abs_ts_time_seconds = e_abs_ts_time_seconds[1:]
    e_abs_time_str = e_abs_ts_time.utc_strftime('%Y-%m-%d-%H:%M:%S')[:-2] + e_abs_ts_time_seconds
    expected_abs_time_str = e_time_str.split('.', 1)[0]
    if e_abs_time_str != expected_abs_time_str:
        print(f"\033[33;1mWARNING: EPHEM abs time as str: {e_abs_time_str!r} != {expected_abs_time_str!r}\033[m")

    e_time = ts.utc(
        e_datetime.year, e_datetime.month, e_datetime.day,
        e_datetime.hour, e_datetime.minute, e_datetime.second)
    if abs(e_time - e_abs_ts_time) > .001:
        print(f"WARNING: unexpected time difference: {e_time} - {e_abs_ts_time}")

    # Compute position to validate the content of the packet
    print(f"   EPHEM pos (TEME): {e_px}, {e_py}, {e_pz}")
    print(f"   EPHEM vel (TEME): {e_vx}, {e_vy}, {e_vz}")

    pos, vel = TEME_to_GCRS(e_time, array([e_px, e_py, e_pz]), array([e_vx, e_vy, e_vz]))
    print(f"   EPHEM pos (GCRS): {pos}")
    print(f"   EPHEM vel (GCRS): {vel}")

    pos, vel, msg = satellite._position_and_velocity_TEME_km(e_time)
    print(f"   Skyfield pos (TEME): {pos}")
    print(f"   Skyfield vel (TEME): {vel}")

    geocentric = satellite.at(e_time)
    print(f"   Skyfield pos (GCRS): {geocentric.position.km}")
    print(f"   Skyfield vel (GCRS): {geocentric.velocity.km_per_s}")

    print("")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cosmos', type=str,
                        help='Connect to Cosmos PREIDENTIFIED router, by default at 127.0.0.1:7779')
    args = parser.parse_args()

    if args.cosmos:
        matches = re.match(r'^([0-9.]+):([0-9]+)$', args.cosmos)
        if not matches:
            parser.error(f"Unexpected Cosmos addr:port {args.cosmos!r}")
        addr = matches.group(1)
        port = int(matches.group(2))
        stream = socket.create_connection((addr, port))
    elif sys.stdin.isatty():
        parser.error("stdin is a TTY, not a stream")
    else:
        stream = sys.stdin.buffer

    print(f"Using sat: {satellite}")

    for ccsds_pkt in pump_cosmos_ccsds_packets(stream):
        apid_name = ccsds_pkt.fieldtype['apid'].i2repr(ccsds_pkt, ccsds_pkt.apid)
        if apid_name == 'EPHEM_TLM_EPHEM':
            print(f"[< {apid_name}] {ccsds_pkt.payload!r}")
            check_ephem(ccsds_pkt.payload)
