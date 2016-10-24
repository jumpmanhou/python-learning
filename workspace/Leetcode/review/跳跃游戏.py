# -*- coding:utf-8 -*-
# 给一个数组a，开始位于起点，在每个位置最多能跳a[i]距离，求是否可以跳到终点

def canJump(nums):
    m = 0
    for i, n in enumerate(nums):
        if m <i:
            return False
        m = max(m,i+n)
        
    return True 
