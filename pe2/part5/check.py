#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import binascii
import string
import math 
import collections

#import solution as student
import deliverable as student

# random.choices added in v3.6
def choices(population,k=1):
    return [random.choice(population) for i in range(k)]

random.choices = choices
######################################################

class TestPart5(unittest.TestCase):


    def setUp(self):
        random.seed(math.pi)

    def test_approximate_pi(self):
        self.assertAlmostEqual(student.approximate_pi(100000),3.14252,places=5)
        self.assertAlmostEqual(student.approximate_pi(10000),3.1412, places=4)
        self.assertAlmostEqual(student.approximate_pi(1000),3.112, places=3)

    def test_letter_count(self):
        txt = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(30,50))])
        correct = collections.Counter(txt)
        self.assertEqual(student.letter_count(txt),correct)

    def test_cut(self):
        filename = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(10,20))])
        txt = '1:2:3\n4:5:6\n7:8:9'
        delimeter = ':'
        fp = io.StringIO(txt)

        def side_effect(givenname,mode='r',**kwargs):
            if filename == givenname:
                return fp
            raise FileNotFoundError

        with unittest.mock.patch('builtins.open',side_effect=side_effect) as m:
            submitted = student.cut(filename,delimeter=delimeter)
            correct = [line.strip().split(delimeter) for line in txt.splitlines()]
            self.assertEqual(submitted,correct)
    
    def test_is_intersecting(self):
        class Circle:
            def __init__(self,x,y,radius):
                self.x = x
                self.y = y
                self.radius = radius
        for _ in range(100):
            c0 = Circle(random.randint(-10,10),random.randint(-10,10),random.randint(1,10))
            c1 = Circle(random.randint(-10,10),random.randint(-10,10),random.randint(1,10))
            correct = math.sqrt((c1.x-c0.x)**2 + (c1.y-c0.y)**2) < (c0.radius + c1.radius)
            self.assertEqual(student.is_intersecting(c0,c1),correct)

    def test_bubble_sort(self):
        l = [random.randint(0,100) for _ in range(30)]
        lcpy = l[:]
        correct = list(sorted(l))
        self.assertEqual(student.bubble_sort(l),correct)
        if l != lcpy:
            self.fail("don't modify the given list")
 
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
