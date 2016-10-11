# -*- coding:utf-8 -*-

# 求BST中两个节点的最小父节点。 
#思路：只要两个节点在当前节点的同一侧，则继续往下找，下一个节点为同一侧的子节点。

def lca(root,p,q):
    while (root.val - p.val)*(root.val -q.val)>0:
        root = (root.left,root.right)[q.val>root.val]
        
    return root

