# -*- coding: utf-8 -*-
# 把一个单链表进行反转
def reverseList(head):
    pre = None
    
    while head:
        cur = head 
        head = head.next
        cur.next = pre
        pre = cur 
        
    return pre

