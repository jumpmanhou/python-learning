# -*- coding: uft-8 -*-
# �������������Ҷ�ӵ�ֵ�ĺ͡��ݹ�

def sumOfLeft(root):
    if not root:
        return 0
    
    res = sumOfLeft(root.left) + sumOfLeft(root.right)
    
    if root.left and not root.left.left and not root.left.right:
        res += root.left.val
        
    return res

