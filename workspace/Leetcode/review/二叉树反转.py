# -*- coding: utff-8 -*-
# 将二叉树的左右子树反转。两种方法：1.递归。2.遍历，用stack 存储节点。

def invertTree(root):
    #recursion
#     if not root:
#         return
#     root.left, root.right = root.right,root.left
#     
#     map(invertTree,(root.left,root.right))

    #Iteration
    
    if not root:
        return 
    stack = [root]
    while len(stack):
        node = stack.pop()
        if node:
            node.left, node.right = node.right,node.left
            stack.append(node.left)
            stack,append(node.right)
            
    return root