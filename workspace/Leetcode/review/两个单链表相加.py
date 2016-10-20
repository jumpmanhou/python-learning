# -*- coding: utf-8 -*- 
# 两个单链表相加，1->2->3(321) + 4->5->6(654) = (975)5->7->9
from compiler.ast import Node

#先把两个链表转换成相应的数字，再把和转换成单链表

def addTwoNumbers(l1,l2):
    def _toInt(node):
        return node.val + _toInt(node.next)*10 if node else 0
    def _toList(n):
        node = ListNode(n%10)
        if n>9:
            node.next = _toList(n/10)
            
        return Node
    return _toList(_toInt(l1)+_toInt(l2))

