# -*- coding: utf-8 -*-
# 递归，依次求左右子树的最小深度


def minDepth(root):
    if not root:
        return 0
    d = map(minDepth, (root.left,root.right))
    
    return 1+(min(d) or max(d))#注意min和max的位置不能呼唤