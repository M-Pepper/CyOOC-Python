#!/usr/bin/env python3
import hashlib

# SHA256 password hash
HASH='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'

def authenticate(func):
    def auth(*args,**kwargs):
        pwhash = hashlib.sha256(input('Enter password: ').encode('utf-8')).hexdigest()
        if pwhash == HASH:
            return func()
        print('Access denied')
    return auth

@authenticate
def get_resource():
    return 'resource'


if __name__ == '__main__':
    print(get_resource())

