# -*- coding: utf-8 -*-

# 平衡二叉树：每个节点左右子树的高度差不大于1
#定义一个辅助函数树的高度，然后依次根据定义判断每个节点是否平衡

def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right))+1



def isBalanced(root):
    if root == None:
        return True
    if abs(height(root.left)-height(root.right))<=1:
        return isBalanced(root.left) and isBalanced(root.right)
    else:
        return False
        