'''
Created on 2016-8-23

@author: 37942
'''
class Solution(object):
    def singleNumber1(self,nums):
        return 2*sum(set(nums))-sum(nums)
    
    def singlenNumber2(self,nums):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0)+1
            
        for  key ,val in dict.items():
            
            if val == 1:
                return key
            