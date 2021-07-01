#!/usr/bin/env python3

def sentinel():
    return chr(128)

def encode_pgm(msg,coverfilename,outputfilename):
    '''Encodes a message in a PGM file
    Args:
        msg (str): the message to encode
        coverfilename (str): the name of the PGM file on disk to use as the cover
        outputfilename (str): the name of the new PGM file to write
    Returns:
        None
    '''
    pass

def decode_pgm(filename):
    '''Decodes a message hidden in a PGM file
    Args:
        filename (str): the name of the PGM file that contains a hidden message
    Returns:
        str: the message that was encoded in the PGM file
    '''
    pass

if __name__ == '__main__':
    pass
