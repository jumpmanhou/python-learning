# -*- coding:utf-8 -*-
#一个m*n二维迷宫，最开始处于左上角，求到右下角一共有多少中方法

# dynamic programming : dp[0][j] = dp[i][0]= 1
# dp[i][j] = dp[i-1][j]+dp[i][j-1] 
# so we can give all the dp a default value 1
# the code as bellow:

def uniquePath(m,n):
    dp = [[1 for x in range(n)] for x in range(m) ]
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[-1][-1]


# follow up: the maze has some obstacles marked as 1, do it again.
# same way : but first we set all dp to 0.

def uniquePath2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    dp = [[0 for x in range(n)] for x in range(m) ]
    for i in range(m):
        if matrix[i][0] ==0:
            dp[i][0] =1
        else:
            break
    for j in range(n):
        if matrix[0][j] == 0:
            dp[0][j] = 1
        else:
            break
        
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] ==1:
                dp[i][j]= 0
            else: 
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
    
    return dp[-1][-1]

print (uniquePath2([[0,0,0],[0,1,0],[0,0,0]]))
    