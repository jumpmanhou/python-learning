# -*- coding: utf-8 -*-
# 判断一个链表中是否有环: 快慢指针，如果有环的话慢指针和快指针会重合


def hasCycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if fast == slow:
            return True
        
    return False