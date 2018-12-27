# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        step=n-m
        if step==0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        m-=1
        n-=1
        while m>0:
            m-=1
            p=p.next
        q=p.next
        while step>0:
            tmp=q.next
            q.next=q.next.next
            tmp.next=p.next
            p.next=tmp
            step-=1
        return dummy.next

