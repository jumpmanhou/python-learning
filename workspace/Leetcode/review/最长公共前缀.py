# -*- coding: utf-8 -*- 
# 找出一组字符串中最长的公共前缀: 先找出字符串中最小的字符串，然后把最小字符串中的字幕依次和剩余字符串进行比较。


def longestCommonPrefix(strs):
    if not strs:
        return ''
    
    first = min(strs)
    
    for i in range(len(first)):
        for s in strs:
            if first[i]!=s[i]:
                return first[:i]
            
    return first


print (longestCommonPrefix(['abc','ab','a','ac']))