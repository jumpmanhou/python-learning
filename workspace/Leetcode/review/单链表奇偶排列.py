# -*- coding: utf-8 -*-

def oddEvenList(head):
    if head:
        odd = head
        even = evenHead = odd.next
        while even and even.next:
            odd.next =odd = odd.next.next
            even.next=even = even.next.next
            odd.next = evenHead
        return head