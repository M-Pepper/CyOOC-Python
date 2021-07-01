#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io

import deliverable as student

class TestPart2(unittest.TestCase):

    def setUp(self):
        self.cover = ['250','251','252','251','250','249','248','249']
        self.stego0 = ['250','251','253','250','250','248','248','249']
        self.msg0 = 'a'
        self.stego1 = ['250', '251', '253', '251', '251', '248', '249', '248']
        self.msg1 = 'z'

    def test_steg_encode_char(self):
        covercpy = self.cover[:]
        student.steg_encode_char(self.msg0,covercpy)
        self.assertEqual(covercpy,self.stego0)

        covercpy = self.cover[:]
        student.steg_encode_char(self.msg1,covercpy)
        self.assertEqual(covercpy,self.stego1)

    def test_steg_decode_char(self):
        answered = student.steg_decode_char(self.stego0)
        self.assertEqual(answered,self.msg0)
        
        answered = student.steg_decode_char(self.stego1)
        self.assertEqual(answered,self.msg1)

if __name__ == '__main__':
    unittest.main()
