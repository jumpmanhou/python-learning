# -*- coding: utf-8 -*- 
# 把1->2->3->4 转换成2->1->4->3

def swapPairs(head):
    dummy = ListNode(0)
    pre, pre.next = dummy, head 
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next,b.next,a.next = b,a,b.next
        pre = a 
        
    return dummy.next