'''
Created on 2016-7-20

@author: 37942
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for num in nums:
            res+= [item+[num] for item in res]
            
        return res
    
s = Solution()

print(s.subsets([1,2,3]))