#!/usr/bin/env python3
import socket

buffer_size = 4096
message = b'Diamond Hands Hodl I Just Like The Stonk To the Moon'
def udp_echo_service():
    while True:
        s = socket.socket(type=socket.SOCK_DGRAM)
        s.bind(('',12345))
        dgram, address = s.recvfrom(4096)
        print('received',dgram,'from',address)
        s.sendto(dgram, address)
        print('sent', dgram,'to',address)


def udp_echo_client():
    for i in range(0, 1000):
        s = socket.socket(type=socket.SOCK_DGRAM)
        dgram = message
        address = ('127.0.0.1',12345)
        s.sendto(dgram,address)
        print('sent', dgram,'to',address)
        echodgram, address = s.recvfrom(4096)
        print('received',echodgram,'from',address)

def tcp_echo_service():
    s = socket.socket()
    s.bind(('',12345))
    s.listen()
    while True:
        conn, address = s.accept()
        print('connection accepted from',address)
        data = conn.recv(buffer_size)
        while data:
            print('received')
            conn.sendall(data)
            print(data,'sent')
            data = conn.recv(buffer_size)

def tcp_echo_client():
    s = socket.socket()
    data = message
    s.connect(('10.50.20.70',12345))
    print('connection established to localhost on port 12345')
    s.sendall(data)
    print(data,'sent')

    accumulated_data = bytearray()
    while accumulated_data != data:
        accumulated_data.extend(s.recv(buffer_size))
        print(accumulated_data,'received')

    s.close()

if __name__ == '__main__':
    #udp_echo_service()
    tcp_echo_client()
