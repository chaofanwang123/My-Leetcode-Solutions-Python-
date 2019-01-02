# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next:
            if p.next.val==val:
                tmp=p.next
                p.next=tmp.next
                tmp=None
            else:
                p=p.next
        return dummy.next
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(1)
head.next.next.next=ListNode(1)
c=Solution().removeElements(head,1)
p=c
while p:
    print(p.val)
    p=p.next   
