#coding:utf8

import hashlib


SHA256 = lambda x : hashlib.sha256(x).digest()

password=b"mysql_passwd"
_password = password
for i in range(5000):
    _password = SHA256(_password)


"""
XOR( SHA256(pwd), SHA256(SHA256(SHA256(pwd))), Nonce)  ?
"""


Nonce = b'\x38\x34\x27\x29\x09\x61\x0d\x44\x16\x2b\x42\x22\x25\x20\x5e\x77\x25\x38\x7b\x05\x00'

_passwordx = b'\x9e\x88\x7d\x0d\x6a\x73\x03\x66\x89\xbd\x56\xb4\xef\x79\x73\xd7\xda\xb1\x75\xde\x13\x25\xd7\x7d\x0d\x8e\xf8\x77\x20\xb9\xf4\x6f'

