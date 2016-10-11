# -*- coding: utf-8 -*-
# 求一个32位无符号整数bit反转后的整数: '{0:032b}'.format(n)

def reverseBits(n):
    oriBit = '{0:032b}'.format(n)
    revBit = oriBit[::-1]
    return int(revBit,2)


print (reverseBits(4526843726))

