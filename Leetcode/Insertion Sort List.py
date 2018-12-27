# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p=head
        while p.next:
            while p.next and p.next.val>=p.val:
                p=p.next
            if not p.next:
                break
            value=p.next.val
            dummy=ListNode(-100)
            dummy.next=head
            q=dummy
            while q.next and value>q.next.val:
                q=q.next
            tmp=p.next
            p.next=p.next.next
            tmp.next=q.next
            q.next=tmp
            head=dummy.next
        return head
head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)
c=Solution().insertionSortList(head)
p=c
while p:
    print(p.val)
    p=p.next
            

