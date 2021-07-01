#!/usr/bin/env python3

import string

class Steg:

    def _fields(self):
        '''Yields the names of PGM header fields one at a time
        Args:
            None
        Returns:
            None
        Yields:
            str: names of PGM header fields
        '''
        yield "magic"
        yield "width"
        yield "height"
        yield "maxval"

    def raster_index(self, data):
        '''Parses a PGM header and returns the index of the first pixel in the raster
        Args:
            data (bytes-like): PGM file data
        Returns:
            int: index of the first pixel
        '''
        i = iter(data)
        token = bytearray()
        tokens = []
        index = 0
        fieldgen = self._fields()
        field = next(fieldgen)

        for b in i:
            index += 1
            if b == 35: # ASCII 35 is a pound sign
                for c in i:
                    index += 1
                    if c in [10,13]: # ASCII 10 and 13 are newline and carriage return
                        break
            elif b in string.whitespace.encode('ascii'):
                try:
                    tokens.append((field,token))
                    field = next(fieldgen)
                except:
                    return index
                token = bytearray()
            else:
                token.append(b)

        return index

    def encode(self, msg, infile, outfile):
        '''LSB encodes a message
        Args:
            msg (bytes): bytes object to encode
            infile (str): name of the raw PGM file on disk to use as the cover
            outfile (str): name of the new PGM file to write
        Returns:
            None
        '''
        pass

    def decode(self, infile):
        '''LSB decodes a message
        Args:
            infile (str): name of the PGM file to read/decode
        Returns:
            bytes: message that was decoded from the PGM file
        '''
        pass

