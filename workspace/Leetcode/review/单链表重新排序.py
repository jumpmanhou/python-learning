# -*- coding:utf-8 -*- 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 思路： 1 快慢指针找到中点
# 2.将后一半倒序
# 3 合并两个链表

def reorderList(head):
    if not head:
        return 
    # find the mid
    fast = slow = head 
    while fast and fast.next:
        slow  = slow.next
        fast = fast.next.next
        
    # reverse the second half 
    pre, node = None,slow
    while node:
        pre,node.next,node = node,pre,node.next
        
    # merge the two halves
    first,second = head, pre
    
    while second.next:
        first.next,first,seond.next,second = second,first.next,first.next,second.next
        
    return