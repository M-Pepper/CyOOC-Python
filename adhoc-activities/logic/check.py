#!/usr/bin/env python3
import itertools
import unittest
import random
import platform

import deliverable as student

version = platform.python_version().split('.')
if int(version[0]) < 3 or int(version[1]) < 6:
    def choices(population,k=1):
        return [random.choice(population) for _ in range(k)]
    random.choices = choices

class Test(unittest.TestCase):
    
    def setUp(self):
        self.valid_codes = []
        for possible in itertools.permutations('01234',5):
            if int(possible[1]) == int(possible[0])*2 and int(possible[2]) < int(possible[4]):
                self.valid_codes.append(''.join(possible))

    def test_validate(self):
        for valid_code in self.valid_codes:
            with self.subTest(code=valid_code):
                self.assertTrue(student.validate(valid_code))
        
        # random tests
        digits = '012345'
        for test in range(20):
            code = ''.join(random.choices(digits,k=5))
            correct = code in self.valid_codes
            with self.subTest(code=code):
                self.assertEqual(student.validate(code),correct)

if __name__ == '__main__':
    unittest.main()
