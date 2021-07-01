#!/usr/bin/env python3
import random

def guess_number(magic_num):
    print(magic_num)
    while True:
        temp_guess = int(input('Enter a number from 0 to 100: '))
        if temp_guess == magic_num:
            print('WIN')
            break
        elif temp_guess > magic_num:
            print('too high')
        elif temp_guess < magic_num:
            print('too low')

guess_number(random.randint(0,100))
