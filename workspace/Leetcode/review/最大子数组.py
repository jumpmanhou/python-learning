# -*- coding: utf-8 -*-
# 给一个数组，求子数组相加最大的和
# 一个记录到当前元素可以得到的最大值，一个记录最大值，最后返回最大值


def maxSub(nums):
    if not nums:
        return 0 
    
    cursum=maxsum = nums[0]
    for i in range(1,len(nums)):
        cursum = max(nums[i],nums[i]+cursum)
        maxsum = max(maxsum, cursum)
    return maxsum


print (maxSub([-2,1,-3,4,-1,2,1,-5,4]))