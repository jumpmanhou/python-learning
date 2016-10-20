# -*- coding: utf-8 -*-
# 1.判断一个单链表中是否有环
# 快慢指针，如果有环的话会在环中的某个节点相遇

def hasCycle(head):
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False


# 2.如果有环，返回环的入口，如果没有，返回none
'''
head到环路起点的距离为K，起点到fast和slow的相遇点的距离为M，环路周长为L。
假设，在fast和slow相遇时，fast走过了Lfast，slow走过了Lslow。根据题意：

　　　　　Lslow=K+M；Lfast=K+M+n*L（n为正整数）；Lfast=2*Lslow

　　　　   可以推出：Lslow=n*L；K=n*L-M

　　　　　则当slow重新回到head，而fast还在相遇点，slow和fast都向前走，且每次走一个节点。

　　　　   则slow从head走到起点走了K，而fast从相遇点出发也走了K，而fast向前走了距离K后到了哪里呢？
由于K=（n-1）*L+（L-M），所以fast转了n-1圈，再走L-M，也到了起点。这样起点就找到了。
'''


def detectCycle(head):
    if head == None or head.next == None:
        return 
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        
        if fast == slow:
            break
    if fast == slow:
        slow = head 
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow 
    return 