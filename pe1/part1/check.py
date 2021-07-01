#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io

import deliverable as student

class TestPart1(unittest.TestCase):
    def setUp(self):
        self.data0 = ('100','200','250')
        self.correct0 = ('155','55','5')
        self.data1 = ('0','45','226','58','131','100','62','70','199','2')
        self.correct1 = ('255', '210', '29', '197', '124', '155', '193', '185', '56', '253')

    def test_inverted(self):
        data = list(self.data0)
        answered = student.inverted(data)
        self.assertEqual(answered,list(self.correct0))
        self.assertEqual(data,list(self.data0))

        data = list(self.data1)
        answered = student.inverted(data)
        self.assertEqual(answered,list(self.correct1))
        self.assertEqual(data,list(self.data1))

    def test_invert(self):
        data = list(self.data0)
        student.invert(data)
        self.assertEqual(data,list(self.correct0))

        data = list(self.data1)
        student.invert(data)
        self.assertEqual(data,list(self.correct1)) 

if __name__ == '__main__':
    unittest.main()
