# -*- coding: utf-8 -*- 
# 给一个unix 类型的文件路径，求出这个路径的最简格式

def simplifyPath(path):
    stack = []
    for item in path.split("/"):
        if item not in ['.','..','']:
            stack.append(item)
        if item =='..':
            stack.pop()
            
    return '/'+'/'.join(stack)
