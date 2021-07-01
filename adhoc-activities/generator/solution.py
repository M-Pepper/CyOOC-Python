#!/usr/bin/env python3

def fib():
    '''
    Generator that yields the fibonacci sequence forever
    '''
    pass
    a, b = 0,1
    while True:
        yield a
        a,b = b, a+b

if __name__ == '__main__':
    fibgen = fib()
    for i in range(17):
        print(next(fibgen))



