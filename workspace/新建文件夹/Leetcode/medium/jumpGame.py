'''
Created on 2016-7-12

@author: 37942
'''
def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal


def canJump2(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

nums = [3,2,1,0,4]

print (canJump2(nums))