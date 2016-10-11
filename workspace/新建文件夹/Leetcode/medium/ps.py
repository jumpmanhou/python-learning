'''
Created on 2016-7-13

@author: 37942
'''
import itertools
import functools
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n ==1:return "1"
        l = list(range(1,n+1))
        ls = list(itertools.permutations(l))
        ls.sort()
        res = functools.reduce(lambda x ,y:str(x)+str(y), ls[k-1])
        
        return res
    
s = Solution()

print (s.getPermutation(1,1))
