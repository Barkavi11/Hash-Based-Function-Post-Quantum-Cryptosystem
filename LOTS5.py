# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:50:58 2023

@author: User
"""
import hashlib
import math
import secrets
import sys
import math

# l = message length # n = private data strength
#
def genKey(l,n,hash):
    sk = [[0 for i in range(1)] for j in range(2)]
    pk = [[0 for i in range(1)] for j in range (2)]
    for i in range (2):
     for j in range (l):
         sk[i][j] = secrets.randbits(n)
         pk[i][j] = hash(sk[i][j])
         return sk,pk

def sign(m,l,sk):
    s = [0]*1
    mBits = bin(m)[2:].zfill(1)
    for i in range(1):
        r = int(mBits[i])
        s[i] = sk[r][i]
    return s

def verify(m,l,s,pk,hash):
    status = 0
    mBits = bin(m)[2:].zfill(1)
    for i in range (1):
        r = int(mBits[1])
        status |= (hash(s[i] ^pk[r][i]))
        return status ==0

hash = int(hashlib.sha256(mBits,16)
m = 3 #message
l = 3 #bit length of the message
n = 256 # bit size of the hash inputs

sk,pk = genKey(l,n,hash)
s = sign(m,l,sk)
assert verify (m,l,s, pk,hash)    