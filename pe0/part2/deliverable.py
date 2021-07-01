#!/usr/bin/env python3

def fizzbuzz(user_num):
    if user_num%5 > 0 and user_num%3 > 0:
        return (user_num)
    elif user_num%5 == 0 and user_num%3 == 0:
        return 'fizzbuzz'
    elif user_num%5 == 0:
        return 'buzz'
    elif user_num%3 == 0:
        return 'fizz'

fizzes = []

while True:
    i = int(input('Enter a number (or 0 to exit): '))
    if i == 0:
        break
    result = fizzbuzz(i)
    if result == 'fizz':
        fizzes.append(i)

print(fizzes)
