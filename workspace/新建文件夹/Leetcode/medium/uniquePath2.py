'''
Created on 2016-7-14

@author: 37942
'''
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        elif m == 1 and n == 1:
            return 1
        
        paths = [[] for i in range(m)] 
    #first col.    
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                while(i < m):
                    paths[i].append(0)
                    i += 1
                break;
            else:
                paths[i].append(1)
   #first row      
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                while(j < n):
                    paths[0].append(0)
                    j += 1
                break;
            else:
                paths[0].append(1)
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i].append(0)
                else:
                    paths[i].append(paths[i][j - 1] + paths[i - 1][j])
                    
        return paths[m - 1][n - 1]

#def uniquePathsWithObstacles(obstacleGrid):
#    m, n, dp = len(obstacleGrid), len(obstacleGrid[0]), [0, 1]
#    dp += [0] * (n - 1)
#    for i in range(1, m + 1):
#        for j in range(1, n + 1):
#            dp[j] = (not obstacleGrid[i-1][j-1]) * (dp[j] + dp[j-1]) 
#    return dp[-1]

s = Solution()


print(s.uniquePathsWithObstacles([[0,0,1,0],[1,0,0,1],[0,0,0,0]]))