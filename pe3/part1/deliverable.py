#!/usr/bin/env python3

import pcap
import socket
import struct

def write_pcap(filename, packet):
    #Populate pcap header with data
    #Populate pcap packet header with data
    #Pack data into struct
    #Write data to the pcap output file
    pass

def createSmurfAttack():
    filename = 'packet.pcap'
    #Populate the header values with data
    #Pack data into struct
    #Calculate checksum using pcap.in_checksum
    #Repack data into structures
    #Write the buffer to file using write_pcap()
    pass



if __name__ == '__main__':
    pass

