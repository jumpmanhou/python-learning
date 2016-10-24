# -*- coding:utf-8 -*-

#荷兰国旗问题：现在有若干个红、白、蓝三种颜色的球随机排列成一条直线。
#现在我们的任务是把这些球按照红、白、蓝排序。
# 思路： 把0排到左边，2排到右边，中间的1自动排列好
# 详细说明链接：http://www.cnblogs.com/gnuhpc/archive/2012/12/21/2828166.html

def sortColors(nums):
    begin = cur = 0
    end = len(nums)-1
    while (cur <= end):
        if nums[cur] == 0:
             nums[begin],nums[cur] = nums[cur],nums[begin]
             begin += 1
             cur += 1
        elif nums[cur]==1:
            cur += 1
        else :
            nums[cur],nums[end] = nums[end],nums[cur]
            end -= 1
nums = [0,1,2,1,1,2,1,0]
sortColors(nums)
print nums