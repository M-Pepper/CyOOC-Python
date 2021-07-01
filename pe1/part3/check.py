#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io

import deliverable as student

class PE1_3(unittest.TestCase):

    def setUp(self):
        self.cover = ['250']*16
        self.stego = [
            '250', '251', '251', '250',
            '250', '250', '250', '251',
            '250', '251', '251', '251',
            '250', '251', '250', '250'
        ]
        self.msg = 'at'

    def test_steg_encode(self):
        student.steg_encode(self.msg,self.cover)
        self.assertEqual(self.cover,self.stego)

    def test_steg_decode(self):
        answered = student.steg_decode(self.stego)
        self.assertEqual(answered,self.msg)

if __name__ == '__main__':
    unittest.main()
