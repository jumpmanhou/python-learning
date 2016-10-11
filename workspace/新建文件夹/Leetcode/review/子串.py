# -*- coding: utf-8 -*-
# 求一个字符串s是否是字符串t的子字符串。
# 例如 abc 是 affhbfljc 的子串 而 acb则不是

def is_subseq(x, y):
#     it = iter(y)
#     return all(c in it for c in x)

    start = 0 
    for char in x :
        start  = y.find(char,start)+1
        
        if not start:
            return False
        
    return True




print (is_subseq('ab', 'afgblgjlclsff'))