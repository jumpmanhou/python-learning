# -*- coding: utf-8 -*- 
# 给定一个集合，求所有的子集

def subSet(nums):
    nums.sort()
    res = []
    dfs(nums,0,[],res)
    return res
    
def dfs(nums,index,path,res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums,i+1,path+[nums[i]],res)
        
        
        
print(subSet([2,1,3]))