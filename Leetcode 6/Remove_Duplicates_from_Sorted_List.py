# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p=head
        while p:
            while p.next and p.next.val==p.val:
                p.next=p.next.next
            p=p.next
        return head    
        
head=ListNode(2)
head.next=ListNode(3)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(3)

c=Solution().deleteDuplicates(head)
p=c
while p:
    print(p.val)
    p=p.next

