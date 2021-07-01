#!/usr/bin/env python3
import unittest
import unittest.mock
import contextlib
import importlib
import sys
import pathlib
import random
import io
import re
import runpy

class TestPart1(unittest.TestCase):

    def fake_input(self):
        yield '15'
        yield '3'
        yield '5'
        yield '7'
        for _ in range(10):
            yield str(random.randint(-100,100))

    def correct(self,i):
        return not i%15 and 'fizzbuzz' or not i%3 and 'fizz' or not i%5 and 'buzz' or i

    def test_fizzbuzz(self):

        for i in self.fake_input():
            with self.subTest(i=i):
                fp = io.StringIO()
                with contextlib.redirect_stdout(fp), unittest.mock.patch('builtins.input',side_effect=[i]):
                    runpy.run_module('deliverable',run_name='__main__')
                    submitted = fp.getvalue()
                    expected = self.correct(int(i))
                    if (not submitted) or (not re.match('{}[\s]*'.format(expected),submitted,re.I)):
                        self.fail('{} is not {}'.format(submitted,expected))

if __name__ == '__main__':
    unittest.main()

