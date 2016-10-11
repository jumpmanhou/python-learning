# -*- coding: utf-8 -*-
# For example, given [1,2,3,4], return [24,12,8,6]
# 要求不能用除法，O(n)时间，O(1)空间
# {              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
# { a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
# Both of which can be done in O(n) by 
# starting at the left and right edges respectively.
# Then multiplying the two arrays element by element gives the required result

def productOfArray(nums):
    p = 1 
    res = []
    n = len(nums)
    #left edge
    for i in range(n):
        res.append(p)
        p *= nums[i]
    # right edge    
    p = 1
    for i in range(n-1,-1,-1):
        res[i] = res[i]*p
        p *= nums[i]
        
    return res


print (productOfArray([1,2,3,4,5]))