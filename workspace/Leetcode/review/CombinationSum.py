# -*-coding: utf-8 -*-
from test.test__locale import candidate_locales

# 返回结果，不包含重复的组合，每个数可以重复使用。 dfs
def combineSum(candidates,target):
    candidates.sort()
    res = []
    dfs(candidates,target,0,[],res)
    return res


def dfs(candidates,target,index,path,res):
    if target<0:
        return 
    if target == 0:
        res.append(path)
        return
    for i in range(index,len(candidates)):
        dfs(candidates,target-candidates[i], i,path+[candidates[i]],res)
        

print (combineSum([2,3,6,7], 7))

# 返回所有组合的个数，不同顺序的组合属于不同的解

#动态规划：

def combineNum1(nums,target):
    nums.sort()
    dp = [0]*(target+1)
    dp[0] = 1
    
    for i in range(1,target+1):
        for num in nums:
            if num > target:
                break
            dp[i] += dp[i-num]
            
            
    return dp[target]
# 组合只能用k个数，每个数只能用一次
def combinationSum3(self, k, n):
    res = []
    self.dfs(xrange(1,10), k, n, 0, [], res)
    return res
    
def dfs(self, nums, k, n, index, path, res):
    if k < 0 or n < 0: # backtracking 
        return 
    if k == 0 and n == 0: 
        res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)