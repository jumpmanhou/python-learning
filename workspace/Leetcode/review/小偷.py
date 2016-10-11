# -*- coding: utf-8 -*- 
#你是一名专业强盗，计划沿着一条街打家劫舍。
#每间房屋都储存有一定数量的金钱，唯一能阻止你打劫的约束条件就是：
#由于房屋之间有安全系统相连，如果同一个晚上有两间相邻的房屋被闯入，它们就会自动联络警察，因此不可以打劫相邻的房屋。
# 用动态规划的思想，到第i间房屋所的钱是now,上一间房屋是last
# 则f(k) = max(f(k-1), f(k-2)+k)
def rub(nums):
    now = last = 0
    
    for i in nums:
        last, now = now, max(now, last +i)
        
    return now


print (rub([5,2,7,9,3,1]))