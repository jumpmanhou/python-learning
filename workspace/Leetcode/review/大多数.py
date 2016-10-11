# -*- coding: utf-8 -*-
# 给一个数组，求数组中出现次数超过2/n 的元素。
from sqlite3 import collections

def majorityEle(nums):
    
    #直接用colletion.Counter().most_common(1)来返回排名第一的元素即可
    #缺点是速度较慢
#     return collections.Counter(nums).most_common(1)[0][0]

    #将数组进行排序，因为多数元素个数大于2/n,所以排在中间的元素即所需元素。
    
#     return sorted(nums)[len(nums)/2]

    #set(nums),然后统计元素在nums中出现的次数，大于n/2则返回该元素。速度较快
    
    num = set(nums)
    
    for n in num:
        if nums.count(n)> len(nums)/2:
            return n
        
        
print (majorityEle([1,2,3,4,5,6,7,7,7,7,7,7,7,7,7]))