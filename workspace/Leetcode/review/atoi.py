# -*- coding: utf-8 -*-
# 将一个字符串转换成对应的整形

def atoi(s):
    if len(s)==0:
        return 0
    ls = list(s.strip())
    sign = 1 if ls[0]!="-" else -1
    if ls[0] in ("+","-"):
        del ls[0]
        
    res =0
    
    for i in ls:
        if i.isdigit():
            res = res*10 +ord(i)-ord("0")
        else:break
        
    return max(-2**31, min(2**31-1, sign*res))

print (atoi(" -12648h4  "))