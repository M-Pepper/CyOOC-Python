#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import re
import contextlib
import nlp

import deliverable as student

class PE1_7(unittest.TestCase):

    def setUp(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            import this
        self.vsm_correct = nlp.vsm(f.getvalue())
        with open('100-0.txt') as fp:
            self.train = fp.read()
        self.ciphertext = '''gur mra bs clguba, ol gvz crgref\n\nornhgvshy vf orggre guna htyl.
rkcyvpvg vf orggre guna vzcyvpvg.\nfvzcyr vf orggre guna pbzcyrk.
pbzcyrk vf orggre guna pbzcyvpngrq.\nsyng vf orggre guna arfgrq.
fcnefr vf orggre guna qrafr.\nernqnovyvgl pbhagf.
fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
nygubhtu cenpgvpnyvgl orngf chevgl.\nreebef fubhyq arire cnff fvyragyl.
hayrff rkcyvpvgyl fvyraprq.\nva gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er qhgpu.
abj vf orggre guna arire.\nnygubhtu arire vf bsgra orggre guna *evtug* abj.
vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!\n'''

    def test_caesar_brute(self):
        answered = student.caesar_brute(self.ciphertext,self.train)
        answered_vsm = nlp.vsm(answered)
        s = nlp.similarity(answered_vsm,self.vsm_correct)
        self.assertTrue(s > 0.80)
    
    def test_prompt(self):
        pass
        #with unittest.mock.patch('builtins.input',
        
if __name__ == '__main__':
    unittest.main()
