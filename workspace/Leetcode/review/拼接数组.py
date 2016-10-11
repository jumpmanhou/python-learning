# -*- coding: utf-8 -*-
#把两个有序数组拼接到一起，使其称为成为一个有序数组。直接在数组1的基础上直接修改。

def merge(num1,m,num2,n):
    while n > 0:
        if m<0 or num1[m-1]<=num[n-1]:
            num1[m+n-1] = num2[n-1]
            n -= 1
        else:
            num1[m+n-1] = num1[m-1]
            m -= 1
            
