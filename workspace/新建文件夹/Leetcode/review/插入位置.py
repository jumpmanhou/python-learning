# -*- coding: utf-8 -*- 
# 给一个有序数组和一个数，求这个数在数组中的位置或者应该插入的位置。

def searchInsert(nums, target):
    return len([x for x in nums if x < target])

