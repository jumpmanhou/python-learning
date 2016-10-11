# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]
  

if __name__ == "__main__":  
    head =ListNode([1,2,3,4,5])      
    s = Solution()
    a =s.removeNthFromEnd(head, 3)
    l=list(a)
    print (l)          