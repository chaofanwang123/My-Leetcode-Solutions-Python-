# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=head
        while p.next:
            tmp=p.next
            p.next=p.next.next
            tmp.next=dummy.next
            dummy.next=tmp
        return dummy.next

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
p=Solution().reverseList(l1)
while p:
    print(p.val)
    p=p.next