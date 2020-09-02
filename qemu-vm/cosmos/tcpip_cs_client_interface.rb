require 'cosmos/interfaces/tcpip_client_interface'
  
module Cosmos

  class TcpipCsClientInterface < TcpipClientInterface

    def write(packet)

          packet.write('CCSDS_CHECKSUM', 0)
          data = packet.buffer
      checksum = 0xFF
          data.each_byte {|x| checksum = checksum ^ x}
      packet.write('CCSDS_CHECKSUM', checksum)

      super(packet)

    end # write()

  end # class

end # module
