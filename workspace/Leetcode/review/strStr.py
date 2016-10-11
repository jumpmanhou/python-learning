# -*- coding: utf-8 -*-
#求短字符串在长字符串中出现的位置。如果没有则返回-1
#技巧：不用一直遍历到最后，只需要遍历len(l)-len(s)次即可，如果还没匹配到，则无法匹配了


def strStr(s,l):
    for i in range(len(l)-len(s)+1):
        if l[i:i+len(s)]==s:
            return i
        
    return -1
    
    
print (strStr("", ""))