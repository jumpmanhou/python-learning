# -*- coding: utf-8 -*-
# 判断两个字符串是不是同型字符串： 用zip()函数。

def sameType(s1,s2):
    
    return len(set(zip(s1,s2)))==len(set(s1)) == len(set(s2))


s1 = "apple"
s2 = "abbtt"

def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

print wordPattern("abba", "dog cat cat dog")

# print (sameType(s1, s2))