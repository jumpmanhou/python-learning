# -*- coding: utf-8 -*-
"""
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

关键是找出规律。
那么，我们通过仔细观察，我们可以得出下面的规律：

F(1) = F(0) + sum - 4D

F(2) = F(1) + sum - 4C

F(3) = F(2) + sum - 4B

那么我们就找到规律了, F(i) = F(i-1) + sum - n*A[n-i]，可以写出代码如下：

"""

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        sums = sum(A)
        sumn = sum(x * n for x, n in enumerate(A))
        ans = sumn
        for x in range(size - 1, 0, -1):
            sumn += sums - size * A[x]
            ans = max(ans, sumn)
        return ans  
    
    
    
s= Solution()
A = [2,4,1,4,5,2,4]
print (s.maxRotateFunction(A))