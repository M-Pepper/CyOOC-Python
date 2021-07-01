#!/usr/bin/env python3

def steg_encode_char(char, cover):
    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        None
    '''
    #1. Get the ascii value for the character
    asc = ord(char)
    #2. Get the binary represenation of the ascii value
    msgbin = '{:08b}'.format(asc)

    for index in range(len(msgbin)):

        #3. Get the binary rpr of the first pixel
        pixelbin = '{:08b}'.format(int(cover[index]))
        #4. Ensure the LSB of the pixel is what we need it to be
        encodedbin = pixelbin[:-1] + msgbin[index]
        #5. Turn the binary pixel back into a number (and back into a string)
        cover[index] = str(int(encodedbin,2))

    pass

def steg_decode_char(stego):
    '''LSB decodes a character
    Args:
        stego (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''
    #1. Accumulate the LSBs
    #2. Transform the acculumated LSBs into a character
    #3. Profit
    bits = []
    for pixels in stego:
        pixelbin = '{:08b}'.format(int(pixels))
        bits.append(pixelbin[-1])
    return chr(int(''.join(bits),2))

    pass

if __name__ == '__main__':
    msg = 'z'
    cover = ['250']*8
    steg_encode_char(msg,cover)
    steg = cover
    print(steg_decode_char(steg))
    pass
    
