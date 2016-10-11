'''
Created on 2016-7-21

@author: 37942
'''
def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


print(removeDuplicates([1,1,1,1,2,3,4,4,5]))