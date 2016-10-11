'''
Created on 2016-7-9

@author: 37942
'''

import itertools
class Solution(object):
    def permute1(self, nums):
        return list(itertools.permutations(nums))
    
    def permute2(self, nums):
        pass
    
s = Solution()

print(s.permute1([1,2,3]))
        
        