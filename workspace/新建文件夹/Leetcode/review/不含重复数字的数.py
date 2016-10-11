# -*- coding: utf-8 -*- 
# 求 0-10**n 之间不含重复数字的数
#f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) f(11) = 0 =f(12)...
# 动态规划： 

def uniqueNumber(n):
    
    nums = [9]
    for i in range(9,0,-1):
        nums.append(nums[-1]*i)
        
    return sum(nums[:n])+1


print (uniqueNumber(6))