'''
Created on 2016-7-3

@author: 37942
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left , right = 0, len(height )-1
        Area = 0
        
        while left < right:
            tmp =(right - left)*min(height[right], height[left])
            Area = max(tmp, Area)
            
            if height[left]< height[right]:
                    left += 1
                    
            else: right -= 1
            
        return Area
    
height = [2,4,1,4,2,6]
s = Solution()
print(s.maxArea(height))
                    
                    