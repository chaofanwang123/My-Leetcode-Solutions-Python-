# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0:
            return head
        p=head
        while n>0:
            n-=1
            p=p.next
        if not p:
            return head.next
        p0=head
        while p.next:
            p=p.next
            p0=p0.next
        p0.next=p0.next.next
        return head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
n=3
c=Solution().removeNthFromEnd(head,n)