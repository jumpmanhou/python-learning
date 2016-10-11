def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = set(nums)
        for num in snums:
            if nums.count(num)>len(nums)/2:
                return num
            
print(majorityElement([2,2,2,1,4]))