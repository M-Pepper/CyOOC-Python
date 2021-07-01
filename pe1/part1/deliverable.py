#!/usr/bin/env python3

def invert(l):
    index = 0
    l = [int(i) for i in l]
    for nums in l:
        l[index] = 255 - l[index]
        index += 1
    l = [str(i) for i in l]

#invert(['100','200','250'])

def inverted(l):
    index = 0
    newl = [int(i) for i in l]
    for nums in newl:
        newl[index] = 255 - newl[index]
        index += 1
    newl = [str(i) for i in newl]
    return newl

#inverted(['100','200','250'])

if __name__ == '__main__':
    pass


for index in range(len(l)):
    l[index] = str(255 - int(l[index]))

newl = []
for pixel in l:
    newl.append(str(255 - int(pixel)))
