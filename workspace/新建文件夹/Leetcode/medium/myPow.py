'''
Created on 2016-7-11

@author: 37942
'''
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
    

s = Solution()

print(s.myPow(1.5, -3))