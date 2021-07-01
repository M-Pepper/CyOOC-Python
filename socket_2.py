#!/usr/bin/env python3
import socket
import sys

def qotd_client(addr='djxmmx.net',port=17):
    s = socket.socket()
    s.connect((addr,port))

    chunk = s.recv(1)
    msg = bytearray()
    while chunk:
        msg.extend(chunk)
        chunk = s.recv(1)

    print(msg.decode('ascii'))

def daytime(addr='8.8.8.8',port=80):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((addr,port))
    except socket.timeout:
        print('failed to connect')
        sys.exit(1)

    msg = bytearray()
    chunk = s.recv(32)
    while chunk:
        msg.extend(chunk)
        chunk = s.recv(32)

    return msg.decode('ascii')

if __name__ == '__main__':
    #qotd_client()
    print(daytime())
