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
        self.pt0 = 'defend the east wall of the castle'
        
        self.ct0 = 'efgfoe uif fbtu xbmm pg uif dbtumf' # right shifted by 1
        self.ct1 = 'cdedmc sgd dzrs vzkk ne sgd bzrskd' # left shifted by 1

        self.ct2 = 'zabajz pda awop swhh kb pda ywopha' # right shifted by 30
        self.ct3 = 'hijirh xli iewx aepp sj xli gewxpi' # left shifted by 30

    def test_caesar_encrypt(self):
        answered = student.caesar_encrypt(self.pt0,1)
        self.assertTrue((answered == self.ct0) or (answered == self.ct1))

        answered = student.caesar_encrypt(self.pt0,30)
        self.assertTrue((answered == self.ct2) or (answered == self.ct3))

    def test_caesar_decrypt(self):
        answered0 = student.caesar_decrypt(self.ct0,1)
        answered1 = student.caesar_decrypt(self.ct1,1)
        self.assertTrue((answered0 == self.pt0) or (answered1 == self.pt0))

        answered0 = student.caesar_decrypt(self.ct2,30)
        answered1 = student.caesar_decrypt(self.ct3,30)
        self.assertTrue((answered0 == self.pt0) or (answered1 == self.pt0))

        
if __name__ == '__main__':
    unittest.main()
