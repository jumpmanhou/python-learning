# -*- coding: utf-8 -*-
# 求一个字符串中第一个不重复字符的位置，如果不存在则返回-1.用一个字典记录出现的次数，然后遍历字符串在字典中的次数


def firstUnique(s):
    
    d = {}
    for char in s:
        d[char] = d.get(char,0)+1
        
    for i, v in enumerate(s):
        if d[v] == 1:
            return i
        
    return -1
    
    
print (firstUnique("leetcode"))

