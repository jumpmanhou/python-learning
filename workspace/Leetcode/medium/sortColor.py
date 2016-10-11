'''
Created on 2016-7-19

@author: 37942
'''
def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1


nums = [1,1,0,2,2,0,1,0,2]
sortColors(nums)
print("Done")
 