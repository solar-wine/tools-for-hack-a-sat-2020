#!/bin/sh
set -e
cd "$(dirname -- "$0")"
flake8 --max-line-length=120 --ignore=F405,E501,F403 ./*.py
