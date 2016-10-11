# -*- coding: utf-8 -*-
#将一个字符串中的元音字幕位置呼唤.

def reverseVowels(s):
    vo = "AEIOUaeiou"
    l,r = 0,len(s)-1
    #string 不可变，把它换成可变的list
    ls = list(s)
    
    while l<r:
        while ls[l] not in vo and l<r:
            l += 1
        while ls[r] not in vo and l<r:
            r -= 1
            
        ls[l],ls[r] = ls[r],ls[l]
        l += 1
        r -= 1
    
    return ''.join(ls)

print (reverseVowels("letcode"))