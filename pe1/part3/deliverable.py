#!/usr/bin/env python3

def steg_encode(msg, cover):
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    coverindex = 0
    for char in msg:
        asc = ord(char)
        msgbin = '{:08b}'.format(asc)
        for index in range(len(msgbin)):
            pixelbin = '{:08b}'.format(int(cover[coverindex]))
            encodedbin = pixelbin[:-1] + msgbin[coverindex]
            cover[coverindex] = str(int(encodedbin,2))
            coverindex += 1

    pass

def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    bits = ''
    chars = ''
    for pixel in stego:
        pixelbin = '{:08b}'.format(int(pixel))
        bits += pixelbin[-1]

        if len(bits) == 8:
            chars += chr(int(bits, 2))
            bits = ''
    return chars

    pass

if __name__ == '__main__':
    pass
