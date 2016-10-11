'''
Created on 2016-7-9

@author: 37942
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for i, d1 in enumerate(num1[::-1]):
            tmp = int(d1)*(10**i)
            for j, d2 in enumerate(num2[::-1]):
                res += tmp * (int(d2)*(10**j))
        return str(res)
    
    
s = Solution()
print(s.multiply("25", "12"))