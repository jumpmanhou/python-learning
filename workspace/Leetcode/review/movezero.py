# -*- coding: utf-8 -*-
# 移动数组中的0到末尾，其他数字位置保持不变。方法：重写cmp函数，然后调用sort(cmp)


def moveZero(nums):
    
    nums.sort(cmp = lambda x,y: -1 if y==0 else 0)

