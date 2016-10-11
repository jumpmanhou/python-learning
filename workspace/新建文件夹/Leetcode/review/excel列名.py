# -*- coding: utf-8 -*-
#给一个正整数,返回对应的列的名称1:A,2:b....26:Z,27:AA...

def convertToTille(n):
    capitals = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    res= []
    while n >0:
        res.append(capitals[(n-1)%26])
        n= (n-1)/26
        
    res.reverse()
    return ''.join(res)


print(convertToTille(333))

# 给列名，求列号

def convertToNum(s):
    ans = 0
    s = s[::-1]
    for i ,v in enumerate(s):
        ans += (ord(v)-64)*(26**i)
        
    return ans

print (convertToNum('LU'))