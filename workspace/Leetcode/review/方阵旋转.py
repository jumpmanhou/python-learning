# -*- coding:utf-8 -*-
# 给一个n*n的方阵，将其顺时针旋转90度，在原地修改

# 思路： 先找一个3*3的方阵手动换一下，发现只需要先将矩阵的行倒序，然后d[i][j] = d[j][i] 即可。

def rotate(matrix):
    
    matrix.reverse()
    
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            



matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotate(matrix)   

print 'done'         