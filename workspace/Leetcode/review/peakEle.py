def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 1, len(nums)-1
        res = []
        
        while i<j:
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                res.append(nums[i])
                i +=2
            else:
                i +=1
                
        return res
    
    
print (findPeakElement([1,2,1,2,1,3,2]))