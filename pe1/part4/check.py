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

class PE1_4(unittest.TestCase):

    def setUp(self):
        self.filename = 'sample.pgm'
        self.header = ['P2','3','3','255']
        self.pixels = [
            '250','250','250',
            '250','250','250',
            '250','250','250'
        ]
        self.filedata = '\n'.join([str(c) for c in self.header+self.pixels])

    def test_read_pgm(self):
        def gen_mock_files():
            while True:
                yield io.StringIO(self.filedata[:])

        fp = gen_mock_files()
        with unittest.mock.patch('builtins.open',side_effect=fp):
            answered = student.read_pgm(self.filename)

            self.assertIsNotNone(answered)
            self.assertIsInstance(answered,tuple)
            self.assertEqual(len(answered),2)
            self.assertEqual(answered,(self.header,self.pixels))

    def test_write_pgm(self):
        fp = io.StringIO()
        mockfileobj = unittest.mock.MagicMock(wraps=fp)
        mockfileobj.__enter__.return_value = mockfileobj
        mockfileobj.close.return_value = None
        
        with unittest.mock.patch('builtins.open',return_value=mockfileobj) as m:
            student.write_pgm('sample.pgm',(self.header[:],self.pixels[:]))
            
            answered = fp.getvalue()
            answered = list(map(str,answered.split()))
            self.assertEqual(answered,self.header+self.pixels)

    def test_invert(self):
        answered = (self.header[:],self.pixels[:])
        student.invert(answered)
        correct = (self.header,[str(255-int(c)) for c in self.pixels])
        self.assertEqual(answered,correct)

if __name__ == '__main__':
    unittest.main()
