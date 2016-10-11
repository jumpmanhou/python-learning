
'''The general idea is:

step1 : copy an array, and sort it using quick sort, O(nlogn) 

step2 : using start and end points to find a, b which satifys a+b==target, O(n)

step3 : find the index of a, b from origin array, O(n)
note: in step3, you should judge whethour a==b, if true, you must find the second index of b.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
        return []
#        nums2 = nums[:]
#        nums2.sort()
#        start = 0
#        end = len(nums)-1
#        a=0
#        b=0
#        while(start<end):
#            sum =nums2[start]+nums2[end]
#            if sum <target:
#                 start+=1  
#            elif sum>target:
#                 end-=1 
#            else:
#                 a = nums2[start]
#                 b = nums2[end]
#                 break
#        res =[]
#        for i in range(len(nums)-1):
#             if (nums[i]==a):
#                
#                 res.append(i)
#                 break
#        if (a!=b):
#             for i in range(len(nums)):
#                  if (nums[i]==b):
#                      res.append(i)
#                      break
#        else :
#            for i in range(len(nums)):
#                    if (nums[i]==b and i!= res[0]):
#                         res.append(i)
#                         break
#        return res        
#                
#        
S = Solution()

l=S.twoSum([0,4,3,0], 0)




    
                