'''
Created on 2016-7-9

@author: 37942
'''
class Solution(object):
    def rotate(self,matrix):
        return [list(col[::-1]) for col in zip(*matrix)]
    
s = Solution()

print (s.rotate([[1,2,3],[4,5,6],[7,8,9]]))