# -*- coding: utf-8 -*-
# 判断两个二叉树是否相同。思路：递归依次判断对应子树是否相同

def isSameTree(p,q):
    if p and q:
        return isSameTree(p.left, q.left) and isSameTree(p.right,q.right)
    
    
    return p is q 

