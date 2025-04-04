# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:06:47 2023

@author: User
"""
import time
import hmac
import hashlib
from binascii import unhexlify, hexlify
from math import ceil, floor, log
from os import urandom

import sys
start = time.time() # Computational time of the algorithm to work
message="Hellow" 

# Algorithms used to create random keys for the signature
if (len(sys.argv)>1):
	message=sys.argv[1]

def sha256(message):
    return hashlib.sha256(message).hexdigest()

def sha256b(message):
    return hashlib.sha256(message).digest()

def random_key(n=32):                   
    return hexlify(urandom(n)) 

#Lamport Key Generation n = 32 byte /256 bits data
def random_lamportkey(numbers=256):      

    private = []
    public = []

    for x in range (numbers):
        #Random Lamport Signature Scheme Keypair is created with urandom(n)
        a,b = random_key(), random_key() 
        #.append() used to increase the only one number 
        private.append((a,b))
        public.append((sha256(a),sha256(b)))

    return private, public

#Lamport Signature Generation n = 32 bytes/256 bits
def sign_lamportkey(private, message):       

    signature = [] 
    bin_lamportmsg = unhexlify(sha256(message))
    print (bin_lamportmsg)
    z = 0
    for x in range (len(bin_lamportmsg)):
        lamport_byte = bin(bin_lamportmsg[x])[2:]      
    # lamport_byte = bin(ord(in_lmsg[x])[2:] #[2:][-1:]     
        while len(lamport_byte) < 8:              
                lamport_byte = '0'+ lamport_byte
        
        for y in range(0,8):
         if lamport_byte[-1:] == '0':
            signature.append(private[z][0])
            lamport_byte = lamport_byte[:-1]
            z+=1
         else:
            signature.append(private[z][1])
            lamport_byte = lamport_byte[:-1]
            z+=1

    return signature

# To Verify Lamport Message Signatures
def verify_lamportkey(signature, message, public ):  #verify lamport signature

    bin_lamportmsg = unhexlify(sha256(message))
    verify = []
    z = 0

    for x in range (len(bin_lamportmsg)):
        #generate a binary string of 8 bits for each byte of 32/256.
        lamport_byte = bin(bin_lamportmsg[x])[2:]  
        # lamport_byte = bin(ord(bin_lamportmsg[x]))[2:] 
        
        while len(lamport_byte) < 8:               #pad the zero's up to 8
                lamport_byte = '0'+ lamport_byte
        
        for y in range(0,8):
         if lamport_byte[-1:] == '0':
            verify.append((sha256(signature[z]),public[z][0]))
            lamport_byte = lamport_byte[:-1]
            z+=1
         else:
            verify.append((sha256(signature[z]),public[z][1]))
            lamport_byte = lamport_byte[:-1]
            z+=1

    for p in range(len(verify)):
        if verify[p][0] == verify[p][1]:
            pass
        else:
            return False    

    return True

message = message.encode()

private,public = random_lamportkey()

print("==== Private key, X =====")
print("Private[0][0] (Set X0): ",private[0][0])
print("Private[0][1] (Set X1):  ",private[0][1])
print("Private[1][0] (Set X0): ",private[1][0])
print("Private[1][1] (Set X1):  ",private[1][1])
print("Private[2][0] (Set X0): ",private[2][0])
print("Private[2][1] (Set X1):  ",private[2][1])
print("Private[3][0] (Set X0): ",private[3][0])
print("Private[3][1] (Set X1):  ",private[3][1])
print("Private[4][0] (Set X0): ",private[4][0])
print("Private[4][1] (Set X1):  ",private[4][1])
print("Private[5][0] (Set X0): ",private[5][0])
print("Private[5][1] (Set X1):  ",private[5][1])

print("==== Public key, Y =====")
print("Public[0][0] (Set Y0): ",public[0][0])
print("Public[0][1] (Set Y1):  ",public[0][1])
print("Public[1][0] (Set Y0): ",public[1][0])
print("Public[1][1] (Set Y1):  ",public[1][1])
print("Public[2][0] (Set Y0):  ",public[2][0])
print("Public[2][1] (Set Y1):  ",public[2][1])
print("Public[3][0] (Set Y0): ",public[3][0])
print("Public[3][1] (Set Y1):  ",public[3][1])
print("Public[4][0] (Set Y0): ",public[4][0])
print("Public[4][1] (Set Y1):  ",public[4][1])
print("Public[5][0] (Set Y0): ",public[5][0])
print("Public[5][1] (Set Y1):  ",public[5][1])

print("==== Message to sign ===============")
print("Message:\t",message)
print("Message digest after hashed by SHA-256:\t",sha256(message))
print("==== Signature =====================")

sign = sign_lamportkey(private,message)

print("Sign[0]:\t",sign[0])
print("Sign[1]:\t",sign[1])
print("Sign[2]:\t",sign[2])
print("Sign[3]:\t",sign[3])
print("Sign[4]:\t",sign[4])
print("Sign[5]:\t",sign[5])
print("The signature test is ",verify_lamportkey(sign,message,public))
end = time.time()
total_time = end - start
print(str(total_time))