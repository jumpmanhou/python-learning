# -*- coding: utf-8 -*-

def mergeSortedList(l1,l2):
    # 如果有空的list,则返回另一个。
    if not l1 or l2:
        return l1 or l2
    cur = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        else:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
    if l1 == None:
        cur.next = l2
    if l2 == None:
        cur.next = l1 
        
    return dummy.next