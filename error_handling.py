#!/usr/bin/env python3
import random

'''print('begin')

try:
    with open('dne.txt', 'r') as whatever:
        pass
    print(1/0)
except ZeroDivisionError as ZeroErr:
    print(ZeroErr)
    print('you tried to divide by zero you goof')
except FileNotFoundError as FileErr:
    print(FileErr)
    print('you tried to open a file that does not exist you goof')

print('fin')'''

def guess_number(n):
    while True:
        try:
            guess = int(input('Enter a number: '))
        except ValueError as ValError:
            print('You didn' + "'" + 't provide a number you goof')
            print(ValueError)
            continue
        if guess == n:
            print('win')
            return
        elif guess > n:
            print('too high')
        else:
            print('too low')

guess_number(random.randint(0,100))
