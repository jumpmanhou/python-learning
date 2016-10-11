# -*- coding: utf-8 -*-
# 移除单链表的倒数第n个元素： 两个指针p1,p2,p1先移动n位，然后p1和p2同时移动
# 当p1到末尾时，p2指向的元素即位要移除的元素



def removeNthFromEnd(head,n):
    dummy = ListNode(0)
    dummy.next = head
    p1=p2=dummy
    for i in range(n):
        p1 = p1.next
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    
    return dummy.next

# 移除单链表中值位val的元素。

def removeElements(head, val):
    dummy = cur = ListNode(0)
    dummy.next = head 
    
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return dummy.next
    
    
    
    
    
    