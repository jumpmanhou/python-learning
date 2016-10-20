# -*- coding: utf-8 -*- 
# 求一个二叉树的右视图。思路： 一层一层遍历，然后把每一层的最后一个元素取出来。

def rightSideView(root):
    view  = []
    if root: 
        level = [root]
        while level:
            view.append(level[-1].val)
            level = [kid for node in level for kid in (node.left,node.right) if kid]
            
    return view 