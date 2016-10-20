# -*- coding:utf-8 -*- 
def intersectionNode(headA,headB):
    if not headA or not headB:
        return None
    pa = headA
    pb = headB
    while pa is not pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
        
    return pa 
        