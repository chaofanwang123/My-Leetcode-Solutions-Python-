# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy=ListNode(0)
        dummy.next=l1
        p=dummy
        q=l2
        while p.next and q:
            if p.next.val<q.val:
                p=p.next
            else:
                tmp=q
                q=q.next
                tmp.next=p.next
                p.next=tmp
                p=p.next
        if not q:
            return dummy.next
        p.next=q
        return dummy.next
            
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
l2=ListNode(2)
l2.next=ListNode(5)
c=Solution().mergeTwoLists(l2,l1)
p=c
while p:
    print(p.val)
    p=p.next