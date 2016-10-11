# -*-coding: utf-8 -*-
#移除有序数列中重复的元素，并返回剩余数组的长度
#用一个tail记录当前的最大长度

def removeDup(nums):
    if not nums:
        return 0
    tail =0
    
    for i in range(1,len(nums)):
        if nums[i]!=nums[tail]:
            tail+=1
            nums[tail]= nums[i]

    return tail+1

# 移除链表中重复的元素。

def romoveList(head):
    cur = head 
    while cur:
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
            
    return head
    
# 删除数组中给定的元素，并返回其长度。

def removeEle(nums,val):    
    nums[:] = [x for x in nums if x!=val]
    
    return len(nums)


print (removeEle([3,2,2,3], 3))