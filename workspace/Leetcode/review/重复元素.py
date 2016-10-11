# -*- coding: utf-8 -*-
# 求一个数组中是否包含重复元素，且两个元素之间的距离小于K
from string import rstrip, strip


def duplicate(nums,k):
    d= {}
    
    for i ,v in enumerate(nums):
        if v in d and i -d[v]<=k:
            return True
        else:
            d[v] = i
            
    return False
   
            
nums = [1,2,3,4,5,6,3]

print (duplicate(nums, 2))

