# -*- coding: utf-8 -*-
#求一串括号是否是匹配的。思路：用一个stack来记录右边的括号，如果右边的括号和左边的不匹配就返回false,最后如果stack
#是空的话则完全匹配

def isValid(s):
    stack = []
    dic = {')':'(',']':'[','}':'{'}#这里把右边的括号当成key方便后面字典的操作。
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack ==[] or dic[char]!=stack.pop() :#注意这里的pop()要放在后面！
                return False
            
    return not stack


print (isValid("()[]{}"))