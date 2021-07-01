#!/usr/bin/env python3
import hashlib

# SHA256 password hash
HASH='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'

'''
Write a decorator that, when applied to a function, prompts the
user for a password. Only execute the wrapped function if the
supplied SHA256 hash of the password matches HASH. Otherwise
print 'Access Denied'.
'''



def get_resource():
    return 'resource'

if __name__ == '__main__':
    print(get_resource())

