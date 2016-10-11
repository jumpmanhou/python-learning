# -*- coding: utf-8 -*-
# 将一个整数拆分成至少两个整数的和，求所有拆分因子积的最大值

#dp[i]表示整数i拆分可以得到的最大乘积，则dp[i]只与dp[i - 2], dp[i - 3]两个状态有关

# 得到状态转移方程dp[i] = max(3*dp[i-3],2*dp[i-2])

def intergerBreak(n):
    
    if n <= 3:
        return n-1
    
    dp = [0]*(n+1)
    dp[2],dp[3] = 2,3
    
    for i in range(4,n+1):
        dp[i] = max(3*dp[i-3],2*dp[i-2])
        
    return dp[n]


