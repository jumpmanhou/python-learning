# -*- coding: utf-8 -*-
# 给一个数组，返回两个数相加等于n的下标。条件：有且只有一组解
#常规算法从第一个数开始依次向后遍历，O(n), 用字典记录当前值的位置，只需要遍历一遍即可，O(n)


def twoSum(l,n):
    h ={}
    for i ,v in enumerate(l):
        if n -v in h:
            return [h[n-v],i]
        
        h[v]=i
        
print (twoSum([2,3,4,5,6], 10))