# -*-coding: utf-8 -*-
# 求n的阶乘的末尾有多少个0
# 计算n有多少个5因子

def trailingzeros(n):
    
    return 0 if n ==0 else n/5 + trailingzeros(n/5)



print (trailingzeros(10))