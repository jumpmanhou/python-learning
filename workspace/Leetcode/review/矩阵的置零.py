# -*- coding: utf-8 -*-
# 把二维矩阵中为0的元素所在的行和列全部置为0，要求在原处修改

def setZeros(matrix):
    m, n , firstRowHasZero = len(matrix),len(matrix[0]), not all(matrix[0])
    