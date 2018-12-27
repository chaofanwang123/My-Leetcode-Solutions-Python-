# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        p1=head
        p2=head
        count=1
        while p2.next and p2.next.next and p1.next!=p2.next.next:
            p1=p1.next
            p2=p2.next.next
            count+=1
        if not p2.next or not p2.next.next:
            return
        p2=head
        while p2!=p1.next:
            p2=p2.next
            p1=p1.next
        return p2

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)     
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=head.next.next  

c=Solution().detectCycle(head)
