#!/usr/bin/env python3

from utility import *

def encode_pgm(msg, infile, outfile):
    '''LSB encodes a message
    Args:
        msg (bytes): bytes object to encode
        infile (str): name of the raw PGM file on disk to use as the cover
        outfile (str): name of the new PGM file to write
    Returns:
        None
    '''
    pass

def decode_pgm(infile):
    '''LSB decodes a message
    Args:
        infile (str): name of the PGM file to read/decode
    Returns:
        bytes: message that was decoded from the PGM file
    '''
    pass

if __name__ == '__main__':
    pass
