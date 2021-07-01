#!/usr/bin/env python3

import random
import math

def approximate_pi(count):
    '''Approximates the value of PI using the Monte Carlo method.
    Args:
        count (int): number of random points to generate
    Returns:
        int: calculated approximation of PI
    '''
    hit = 0
    for i = range(count):
        x = (random.random()*2)-1.0
        y = (random.random()*2)-1.0
        if ((x**2)+(y**2))**0.5 <= 1.0:
            hit += 1
    return hit//count*4


def letter_count(txt):
    '''Counts the number of occurances of each letter in the given text
    Args:
        txt (str): text consisting of alpha-numeric characters
    Returns:
        dict: dictionary whose keys are alpha-numeric characters and values are
              the number of occurances encountered in the given text
    '''
    counts = dict()
    for letter in txt:
        counts[letter] += 1
    return counts


# Exception: FileNotFoundError
# Logical: list.extend vs append
def cut(filename, delimeter=':'):
    '''Produces columns of text from lines of text using a delimeter
    Args:
        filename (str): name of the file to read from
        delimiter (str): single character string used to separate columns for each line
    Returns:
        list: list of lists of columns for each line

        Example:
        1:2:3
        4:5:6
        7:8:9
        [['1','2','3'], ['4','5','6'], ['7','8','9']]
    '''
    data = []
    with open('filename','r') as fp:
        data.append([line.strip().split(delimeter) for line in fp.readlines()])
    return data

# Exception: AttributeError
# Logical
def is_intersecting(c0,c1):
    '''Calculates whether 2 circles are intersecting
    Args:
        c0 (Circle): object with x, y, and radius attributes
        c1 (Circle): object with x, y, and radius attributes
    Returns:
        bool: True if the given circles intersect, otherwise False
    '''
    distance = math.sqrt( (c1.x - c0.x)**2 + (c1.y - c0.y)**2 )
    sum_of_radii = c0.radii + c1.radii
    if distance < sum_of_radii:
        return True
    else:
        return False


# Exception: IndexError
# Logical: return statement at the wrong level of indentation
def bubble_sort(l):
    '''Returns a new sorted list using the bubble sort algorithm
    Args:
       l (list): list of integers to sort
    Returns:
        None
    '''
    newlist = l[:]
    for sortpass in range(len(l),0,-1):
        for index in range(sortpass):
            if newlist[index] > newlist[index+1]:
                newlist[index], newlist[index+1] = newlist[index+1], newlist[index]
        return newlist

if __name__ == '__main__':
    pass
