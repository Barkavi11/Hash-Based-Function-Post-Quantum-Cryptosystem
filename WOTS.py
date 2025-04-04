# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:21:52 2022

@author: User
"""
import sys
import time
import hashlib
from binascii import unhexlify, hexlify
from os import urandom
start = time.time()
message="Hellow World ! How are you ?!!!!"

def random_key(n=32):  #returns a 256 bit hex encoded (64 bytes) random number
    return hexlify(urandom(n))

def sha256(message):
    return hashlib.sha256(message.encode()).hexdigest()

def sha256b(message):
    return hashlib.sha256(message.encode()).digest()

def random_wkey(w=8, verbose=0):      #create random W-OTS keypair

    private = []
    public = []
    print("Hashing number random keys by:\t",2**w)
    for x in range(256//w):
        a = str(random_key())
        private.append(a)
        for y in range(2**w-1):              
            a = sha256(a)
        public.append(sha256(a))               

    return private, public 

def sign_wkey(private, message):      

    signature = []
    bin_msg = unhexlify(sha256(message))

    for y in range(len(private)):
        s = private[y]    
        for x in range(256-ord(bin_msg[y:y+1])):
            s = sha256(s)
        signature.append(s)
    return signature

def verify_wkey(signature, message, public):

    verify = []
    bin_msg = unhexlify(sha256(message))
    
    for x in range(len(signature)):
        a = signature[x]
                                                    #f is all but last hash..
        for z in range(ord(bin_msg[x:x+1])):
                a=sha256(a)
        #a = sha256(a)                               #g is the final hash, separate so can be changed..
        verify.append(a)
  
    if public != verify:
        return False

    return True


private, public = random_wkey()

print("==== Private key (keep secret) =====")
print("Private[0]: ",private[0])
print("Private[1]: ",private[1])
print("Private[2]: ",private[2])
print("Private[3]: ",private[3])
print("Private[4]: ",private[4])
print("Private[5]: ",private[5])

print("==== Public key (show everyone)=====")
print("Public[0]: ",public[0])
print("Public[1]: ",public[1])
print("Public[2]: ",public[2])
print("Public[3]: ",public[3])
print("Public[4]: ",public[4])
print("Public[5]: ",public[5])

print("==== Message to sign ===============")
print("Message:\t",message)
print("SHA-256:\t",sha256(message))
print("==== Signature =====================")
sign = sign_wkey(private,message)

print("Signatue[0]:\t",sign[0])
print("Signatue[1]:\t",sign[1])
print("Signatue[2]:\t",sign[2])
print("Signatue[3]:\t",sign[3])
print("Signatue[4]:\t",sign[4])
print("Signatue[5]:\t",sign[5])

print("The signature test is ",verify_wkey(sign,message,public))
end = time.time()
total_time = end - start
print(str(total_time))