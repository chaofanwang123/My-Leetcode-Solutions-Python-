# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next and p.next.next:
            tmp=p.next.next
            p.next.next=tmp.next
            tmp.next=p.next
            p.next=tmp
            p=p.next.next
        return dummy.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

c=Solution().swapPairs(head)
