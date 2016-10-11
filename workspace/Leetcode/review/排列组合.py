# -*- coding:utf-8 -*-
# 给一个没有重复数字的数组，求所有的排列组合。
from timeit import itertools

# dfs 

def permute(nums):
    res = []
    dfs(nums,[],res)
    return res
    
    
    
    
def dfs(nums,path,res):
    
    if not nums:
        res.append(path)
        
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        

print(permute([1,2,3]))
#直接用python中的itertools.permutations函数。
print(map(list,itertools.permutations([1,2,3])))