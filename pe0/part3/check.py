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
import inspect
import runpy

class TestPart2(unittest.TestCase):

    def setUp(self):
        pass

    def make_guess(self):
        # Determine the value actually passed to the deliverable function by the student
        frame = next(finfo.frame for finfo in inspect.stack() if finfo.function == 'guess_number')
        arginfo = inspect.getargvalues(frame)
        self.correct = arginfo.locals[arginfo.args[0]]

        window = [0,100]
        guess = random.randint(*window)
        self.guess = guess
        yield str(guess)

        while guess != self.correct:
            if guess > self.correct:
                window[1] = guess-1
                guess = random.randint(*window)
                self.guess = guess
                yield str(guess)
                continue
            else:
                window[0] = guess+1
                guess = random.randint(*window)
                self.guess = guess
                yield str(guess)
                continue

    def test_game(self):
        fp = io.StringIO()
        with contextlib.redirect_stdout(fp), unittest.mock.patch('builtins.input',side_effect=self.make_guess()) as m:
            
            # NOTE: runpy is needed to allow students to use the if __name__=='__main__' idiom
            #import deliverable as student
            try:
                runpy.run_module('deliverable',run_name='__main__')
            except SystemExit:
                pass
            
            submitted = fp.getvalue()
            submitted = list(map(str.upper,submitted.splitlines()))
            self.assertEqual(submitted[-1],'WIN')
            #m.assert_called()
            self.assertEqual(self.guess,self.correct)

if __name__ == '__main__':
    unittest.main()
