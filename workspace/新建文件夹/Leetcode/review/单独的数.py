# -*-coding: utf-8 -*- 
# 求一个数列中只出现一次的数
from sqlite3 import collections


# (1) 除了要 求的数，每个数都出现两次。
def singleNum(nums):
    return sum(set(nums))*2 -sum(nums)

# (2) 除了要求的数， 每个数都出现3次。
def singleNum(nums):
    return (3*sum(set(nums)) - sum(nums))/2
# (3) 有两个数出现一次，其他数都出现两次
def singleNum(nums):
    return [x[0] for x in collections.Counter(nums).items() if x[1]== 1]