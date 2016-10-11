'''
Created on 2016-7-18

@author: 37942
'''
class Solution(object):
    def searchMatrix(self,matrix,target):
        if not matrix or target == None:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        
        while l<=r:
            mid = (l+r)//2
            num = matrix[mid//2][mid%2]
            if num == target:
                return True
            elif num < target:
                l = mid+1
            else:
                r = mid-1
        return False
    
s = Solution()
matrix = [[1,2,3,4],[5,6,7,8]]
print (s.searchMatrix(matrix, 5))