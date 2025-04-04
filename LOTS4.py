# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:46:26 2022

@author: User
"""
# Notes from https://medium.com/asecuritysite-when-bob-met-alice/lamport-signatures-for-a-post-quantum-computing-world-279cb088570ees from
import time
import hmac
import hashlib
from binascii import unhexlify, hexlify
from math import ceil, floor, log
from os import urandom

import sys
start = time.time()
message="Hellow"

if (len(sys.argv)>1):
	message=sys.argv[1]


def sha256(message):
    return hashlib.sha256(message).hexdigest()

def sha256b(message):
    return hashlib.sha256(message).digest()

def random_key(n=32):                   
    return hexlify(urandom(n))

def sign_lkey(priv, message):       #perform lamport signature
    
    signature = [] 
    bin_lmsg = unhexlify(sha256(message))
    print (bin_lmsg)
    z = 0
    for x in range (len(bin_lmsg)):
        l_byte = bin(bin_lmsg[x])[2:] #[2:][-1:]      
         # l_byte = bin(ord(in_lmsg[x])[2:] #[2:][-1:]        
        while len(l_byte) < 8:              
                l_byte = '0'+ l_byte
        
        for y in range(0,8):
         if l_byte[-1:] == '0':
            signature.append(priv[z][0])
            l_byte = l_byte[:-1]
            z+=1
         else:
            signature.append(priv[z][1])
            l_byte = l_byte[:-1]
            z+=1

    return signature


def verify_lkey(signature, message, pub ):  #verify lamport signature

    bin_lmsg = unhexlify(sha256(message))
    verify = []
    z = 0

    for x in range (len(bin_lmsg)):
        l_byte = bin(bin_lmsg[x])[2:]   #generate a binary string of 8 bits for each byte of 32/256.
        # l_byte = bin(ord(bin_lmsg[x]))[2:] 
        
        while len(l_byte) < 8:               #pad the zero's up to 8
                l_byte = '0'+ l_byte
        
        for y in range(0,8):
         if l_byte[-1:] == '0':
            verify.append((sha256(signature[z]),pub[z][0]))
            l_byte = l_byte[:-1]
            z+=1
         else:
            verify.append((sha256(signature[z]),pub[z][1]))
            l_byte = l_byte[:-1]
            z+=1

    for p in range(len(verify)):
        if verify[p][0] == verify[p][1]:
            pass
        else:
            return False    

    return True

def random_lmkey(numbers=256):      #create random lamport signature scheme keypair

    priv = []
    pub = []

    for x in range (numbers):
        a,b = random_key(), random_key()
        priv.append((a,b))
        pub.append((sha256(a),sha256(b)))

    return priv, pub

message = message.encode()

priv,pub = random_lmkey()
print("==== Private key (keep secret) =====")
print("Priv[0][0] (SetA): ",priv[0][0])
print("Priv[0][1] (SetB):  ",priv[0][1])
print("Priv[1][0] (SetA): ",priv[1][0])
print("Priv[1][1] (SetB):  ",priv[1][1])
print("Priv[2][0] (SetA): ",priv[2][0])
print("Priv[2][1] (SetB):  ",priv[2][1])
print("Priv[3][0] (SetA): ",priv[3][0])
print("Priv[3][1] (SetB):  ",priv[3][1])
print("==== Public key (show everyone)=====")
print("Pub[0][0]: ",pub[0][0])
print("Pub[0][1]:  ",pub[0][1])
print("Pub[1][0]: ",pub[1][0])
print("Pub[1][1]:  ",pub[1][1])
print("==== Message to sign ===============")
print("Message:\t",message)
print("SHA-256:\t",sha256(message))
print("==== Signature =====================")
sign = sign_lkey(priv,message)

print("Sign[0]:\t",sign[0])
print("Sign[1]:\t",sign[1])
print("Sign[2]:\t",sign[2])
print("Sign[3]:\t",sign[3])
print("The signature test is ",verify_lkey(sign,message,pub))
end = time.time()

total_time = end - start
print(str(total_time))