# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:54:23 2022

@author: User
"""
import hashlib
import math
import secrets
import sys
CHAR_ENC ='utf-8' 
# UTF-8 : Unicode Transformation Format ( 8-bit values in the encoding)
# byte oriented encoding that specifies that each character is represented by a specific sequence of one or more bytes. 

BYTE_ORDER = sys.byteorder
SK = 0
PK = 1

#Keypair generation for one-time signature
def keygen():
    sk = [[0 for x in range(256)]for y in range(2)]
    pk = [[0 for x in range(256)]for y in range(2)]
    for i in range(0,256) :
        #secret key generation
        sk[0][i] = secrets.token_bytes(32)
        sk[1][i] = secrets.token_bytes(32)
        #public key generation
        pk[0][i] = hashlib.sha256(sk[0][i]).digest()
        pk[1][i] = hashlib.sha256(sk[1][i]).digest()
        
    keypair = [sk,pk]
    return keypair

#Sign messages using Lamport one-time signatures
def sign(m, sk):
    sig = [0 for x in range(256)]
    h = int.from_bytes(hashlib.sha256(m.encode(CHAR_ENC)).digest(), BYTE_ORDER)
    for i in range(0,256):
        b = h >> i & 1
        sig [i] = sk[b][i]
    return sig

 # Verify Lamport message signatures
def verify(m, sig, pk):
     h = int.from_bytes(hashlib.sha256(m.encode(CHAR_ENC)).digest(), BYTE_ORDER)
     for i in range(0,256):
         b = h >> i & 1
         check = hashlib.sha256(sig[i]).digest()
         if pk[b][i] != check:
             return False
     return True
print
keypair = keygen()
message = "I love mathematics"
sig = sign(message, keypair[SK])
verify(message, sig, keypair[PK])