# -*- coding: utf-8 -*- 
# 给定一个二叉树的中序遍历和后序遍历的结果，求这个二叉树

def buildTree(inorder,postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    ind = inorder.index(root.val)
    root.right = buildTree(inorder[ind+1:], postorder)
    root.left = buildTree(inorder[:ind], postorder)
    
    return root

# 给定前序遍历和中序遍历的结果，求二叉树。

def buildTree2(preoder,inorder):
    if inorder:
        root = preorder.pop(0)
        ind = inorder.index(root.val)
        root.left = buildTree2(preoder, inorder[:ind])
        root.right = buildTree2(preoder, inorder[ind+1:])
        return root