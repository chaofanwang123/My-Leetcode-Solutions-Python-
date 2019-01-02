# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        p=head
        length=1
        while p.next:
            length+=1
            p=p.next
        if k%length==0:
            return head
        p.next=head
        k=k%length
        count=0
        while count<length-k:
            count+=1
            tmp=head
            head=head.next
        tmp.next=None
        return head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

c=Solution().rotateRight(head,5)
p=c
while p:
    print(p.val)
    p=p.next