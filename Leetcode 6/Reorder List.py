# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        p1=head
        p2=head
        while p2.next and p2.next.next:
            p2=p2.next.next
            p1=p1.next
        if p2.next:
            p1=p1.next
        q=p1.next
        while q.next:
            tmp=q.next
            q.next=tmp.next
            tmp.next=p1.next
            p1.next=tmp
        tmp=p1.next
        p1.next=None
        p1=head
        p2=tmp
        while p2:
            tmp2=p2.next
            p2.next=p1.next
            p1.next=p2
            p1=p1.next.next
            p2=tmp2
        return

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
c=Solution().reorderList(head)
p=c
while p:
    print(p.val)
    p=p.next          

