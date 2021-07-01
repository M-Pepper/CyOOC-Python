#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import re

import deliverable as student

class PE1_5(unittest.TestCase):

    def setUp(self):
        self.covername = 'sample.pgm'
        self.coverheader = ['P2','5','5','255']
        self.coverpixels = [
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250'
        ]
        self.coverdata = '\n'.join([str(c) for c in self.coverheader+self.coverpixels])

        self.stegname = 'steg.pgm'
        self.stegheader = ['P2','5','5','255']
        self.stegpixels = [
            '250','251','251','250','250',
            '250','250','251','250','251',
            '251','251','250','251','250',
            '250','251','250','250','250',
            '250','250','250','250','250'
        ]
        self.stegdata = '\n'.join([str(c) for c in self.stegheader+self.stegpixels])

        self.msg = 'at'

    def encode(self,msg,cover):
        '''DO NOT use this code in your solution. And don't write production code that looks like this ;)'''
        return list(map(str,[x if i >= 8*len(msg) else (x | ((ord(msg[i//8]) & (0x80 >> (i%8))) >> 7-(i%8))) for i,x in enumerate(map(int,cover))]))

    def test_decode_pgm(self):
        stegdata = '\n'.join(self.stegheader + self.encode(self.msg+student.sentinel(),self.coverpixels))
        fp = io.StringIO(stegdata)
        with unittest.mock.patch('builtins.open',return_value=fp):
            answered = student.decode_pgm(self.stegname)
            self.assertEqual(answered,self.msg)

    def test_encode_pgm(self):
        coverfp = io.StringIO(self.coverdata)
        stegfp = io.StringIO()
        mockfileobj = unittest.mock.MagicMock(wraps=stegfp)
        mockfileobj.__enter__.return_value = mockfileobj
        mockfileobj.close.return_value = None
        
        def side_effect(filename,mode='r',**kwargs):
            if filename == self.stegname:
                return mockfileobj
            elif filename == self.covername:
                return coverfp
            else:
                raise FileNotFoundError

        with unittest.mock.patch('builtins.open',side_effect=side_effect) as m:
            student.encode_pgm(self.msg,self.covername,self.stegname)
            
            answered = stegfp.getvalue()
            answered = answered.split()

            self.assertEqual(answered[:4],self.stegheader)
            correct = self.encode(self.msg+student.sentinel(),self.coverpixels)
            self.assertEqual(answered[4:],correct)

if __name__ == '__main__':
    unittest.main()
