#!/usr/bin/env python3

import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import socket
import os.path
import contextlib

import deliverable as student
#import solution as student

class TestPart1(unittest.TestCase):
    def setUp(self):
        self.fname = 'bressemers.pgm'
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        self.x0 = random.randint(0, 151)
        self.y0 = random.randint(0, 151)
        self.x1 = random.randint(0, 151)
        self.y1 = random.randint(0, 151)
        self.allpoints = []
        self.content = []
    def img(self):
        maxx = sorted(self.allpoints)[-1][0]
        maxy = sorted(self.allpoints, key=lambda x: x[1])[-1][1]
        pixels = [[0xff for x in range(maxx + 1)] for y in range(maxy + 1)]
        for point in self.allpoints:
            pixels[maxy - point[1]][point[0]] = 0x0
        pixelvalues = [str(y) for x in pixels for y in x]
        self.content = (['P2', '{}'.format(maxx+1), '{}'.format(maxy+1), '255'], pixelvalues)
    def plotLineLow(self, x0,y0, x1,y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2*dy - dx
        y = y0
        for x in range(x0, x1+1):
            self.allpoints.append((x,y))
            if D > 0:
                y = y + yi
                D = D - 2*dx
            D = D + 2*dy
    def plotLineHigh(self, x0,y0, x1,y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2*dx - dy
        x = x0
        for y in range(y0, y1+1):
            self.allpoints.append((x,y))
            if D > 0:
                x = x + xi
                D = D - 2*dy
            D = D + 2*dx
    def plotLine(self, x0,y0, x1,y1):
        if abs(y1 - y0) < abs(x1 - x0):
            self.plotLineLow(x1 if x0 > x1 else x0, y1 if x0 > x1 else y0, x0 if x0 > x1 else x1, y0 if x0 > x1 else y1)
        else:
            self.plotLineHigh(x1 if y0 > y1 else x0, y1 if y0 > y1 else y0, x0 if y0 > y1 else x1, y0 if y0 > y1 else y1)
        self.img()
    def test_pcap(self):
        fp = io.StringIO()
        with contextlib.redirect_stdout(fp):
            student.drawline(self.x0, self.y0, self.x1, self.y1)
        submitted = fp.getvalue()
        submitted = submitted.split()
        while submitted[-1] == '':
            del submitted[-1]
        self.plotLine(self.x0,self.y0, self.x1,self.y1)
        expected = ['{},{}'.format(x,y) for x,y in self.allpoints]
        self.assertEqual(submitted, expected)
        self.assertTrue(os.path.isfile(self.fname), 'File {} does not exist'.format(self.fname))
        with open(self.fname) as fp:
            content = fp.read().split()
        allc = (content[0:4], content[4:])
        self.assertEqual(allc[0], self.content[0])
        self.assertEqual(len(allc[1]), len(self.content[1]))
        print('If the next operation is slow, the pixel values are different. Checking {} pixels'.format(len(self.content[1])))
        self.assertEqual(allc[1], self.content[1])

if __name__ == '__main__':
    unittest.main()
