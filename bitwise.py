#!/usr/bin/env python3
'''def shared_bits(int1, int2):
    bin3 = int1 & int2
    shared_bits = 0
    does_share = False

    for bits in bin(bin3):
        print(bits)
        if bits == '1':
            shared_bits += 1
            if shared_bits >= 2:
                does_share = True
                break
    print(does_share)
    return does_share

shared_bits(100, 255)'''



'''def shared_bits(int1, int2):
    return bin(int1 & int2).count('1') > 1'''

def shared_bits(int1, int2):
    bin3 = int1 & int2
    shared_bits = 0
    for shift in range(bin3.bit_length()-1,-1,-1):
        shared_bits += (bin3 >> shift) & 1
    return shared_bits >= 2

shared_bits(1, 1)
