#!/usr/bin/env python3

ICMP_ECHO = 8
PCAP_VERSION_MAJOR = 2
PCAP_VERSION_MINOR = 4

def in_checksum(header, length):
    sumval = 0
    answer = 0 
    nleft = length
    index = 0
    while (nleft > 1):
        sumval += ((header[index] << 8) | header[index+1])
        nleft -= 2
        index += 2

    if (nleft == 1):
        sumval += header[index]

    sumval = (sumval >> 16) + (sumval & 0xffff)
    sumval += (sumval >> 16)
    answer = ~sumval
    return (answer & 0xffff)

if __name__ == '__main__':
    pass

