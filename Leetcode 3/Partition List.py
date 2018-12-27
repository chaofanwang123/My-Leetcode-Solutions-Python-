# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        dummy2=ListNode(0)
        p1=dummy
        p2=dummy2
        while p1.next:
            if p1.next.val<x:
                p2.next=p1.next
                p2=p2.next
                p1.next=p1.next.next
            else:
                p1=p1.next
        p2.next=dummy.next
        return dummy2.next
                
head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(3)     
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(2)   

c=Solution().partition(head,3)

p=c
while p:
    print(p.val)
    p=p.next