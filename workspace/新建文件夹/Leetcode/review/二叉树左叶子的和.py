# -*- coding: uft-8 -*-
# 求二叉树所有左叶子的值的和。递归

def sumOfLeft(root):
    if not root:
        return 0
    
    res = sumOfLeft(root.left) + sumOfLeft(root.right)
    
    if root.left and not root.left.left and not root.left.right:
        res += root.left.val
        
    return res

