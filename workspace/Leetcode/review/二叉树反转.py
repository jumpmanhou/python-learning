# -*- coding: utff-8 -*-
# ��������������������ת�����ַ�����1.�ݹ顣2.��������stack �洢�ڵ㡣

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