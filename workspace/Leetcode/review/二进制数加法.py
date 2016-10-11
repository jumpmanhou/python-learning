# -*- coding: utf-8 -*-
#求一个二进制数的加法，并返回一个二进制字符串。

def addBin(a,b):
    
#     return bin((eval("0b%s +0b%s"%(a,b))))[2:]
    return bin(int(a,2)+int(b,2))[2:]
    


a= "011001"
b= "1101101"

print addBin(a, b)