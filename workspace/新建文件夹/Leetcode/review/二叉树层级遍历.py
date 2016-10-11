# -*- coding: utf-8 -*-

# 层级遍历二叉树： 用一个stack 来存储当前层数以及节点，层数用来在结果中添加对应的list
# 层级遍历倒转：只需要输出时逆向输出即可res[::-1]

def levelOrder(root):
    res = []
    stack = [(root,0)]
    
    while len(stack):
        node,level = stack.pop()
        if node:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            stack.append((node.right,level+1))
            stack.append((node.left, level+1))
    
    return res


# 二叉树中序遍历: 递归
def helper(root, res):
    if root:
        hepler(root.left,res)
        res.append(root.val)
        helper(root.right,res)
        
def inOrder(root):
    res = []
    helper(root, res)
    return res

#二叉树前序遍历： 递归

def helper1(root,res):
    if root:
        res.append(root.val)
        helper1(root.left, res)
        helper1(root.right,res)
        

def preOrder(root):
    
    res = []
    helper1(root, res)
    return res 



#二叉树后序遍历：递归

def helper2(root, res):
    if root:
        helper2(root.left, res)
        helper2(root.right,res)
        res.append(root.val)

def postOrder(root):
    res=[]
    helper2()
    