# -*- coding: utf-8 -*-
#求出二叉树所有根到叶的路径： dfs(root,"",res) 加递归


def BinPath(root):
    if not root:
        return []
    
    res = []
    dfs(root,'',res)
    
    return res

def dfs(root,ls,res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
        
    if root.left:
        dfs(root.left,ls+str(root.val)+'->',res)
    if root.right:
        dfs(root.right, ls+str(root.val)+'->', res)