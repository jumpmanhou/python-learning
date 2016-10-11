# -*- coding: utf-8 -*-
#求一个矩阵从左上角到右下角的和最小的路径

# 动态规划：dp[0][i] = dp[0][i-1]+grid[0][i]
#        dp[i][0] = dp[i-1][0] +grid[i][0]
#        dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

def minPath(grid):
    if not grid:
        return 
    r, c = len(grid),len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = grid[0][0]
    for i in range(1,r):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1,c):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    for i in range(1,r):
        for j in range(1,c):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[-1][-1]


print(minPath([[1,2,3],[3,2,4],[3,4,1]]))