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

import deliverable as student
#import solution2 as student

class TestPart1(unittest.TestCase):
    def setUp(self):
        self.fname = 'packet.pcap'
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        self.pcapfileheader = (0, 24, b'\xa1\xb2\xc3\xd4\x00\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x65')
        self.pcappackheader = (24, 16, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x1c')
        self.ipheader = (40, 20, b'\x45\x00\x00\x1c\x3a\xa1\x00\x00\xff\x01\xfe\xee\xc0\xa8\x00\x01\xc0\xa8\x00\xff')
        self.icmpheader = (60, 8, b'\x08\x00\xf7\xfd\x00\x01\x00\x01')
        self.ihlval = (0x28, 1, 0xF,  0, 5, 'IHL Version')
        self.ipversion = (0x28, 1, 0xF0, 4, 4, 'IP Version')
        self.ipproto = (0x31, 1, 0xFF, 0, 1, 'IP Protocol')
        self.icmptype = (0x3C, 1, 0xFF, 0, 8, 'ICMP Type')
        self.checks = (self.ihlval, self.ipversion, self.ipproto, self.icmptype)

    def getPcapBytes(self, filename):
        with open(filename, 'rb') as fp:
            return fp.read()

    def validateBytes(self, offset, blen, act, exp):
        for x in range(offset, offset + blen + 1):
            self.assertEqual(act[x], exp[x])

    def test_pcap(self):
        student.createSmurfAttack()
        self.assertTrue(os.path.isfile(self.fname), 'File {} does not exist'.format(self.fname))
        pcapbytes = self.getPcapBytes(self.fname)
        self.assertEqual(len(pcapbytes), 68, 'Length of {} is incorrect'.format(self.fname))
        for check in self.checks:
            self.assertEqual((pcapbytes[check[0]] & check[2]) >> check[3], check[4], 'Invalid: {}'.format(check[5]))

if __name__ == '__main__':
    unittest.main()
