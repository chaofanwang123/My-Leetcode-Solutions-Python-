# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1=head.next
        p2=head
        while p1 and p1.next:
            tmp=p1.next
            p1.next=p1.next.next
            p1=p1.next
            tmp.next=p2.next
            p2.next=tmp
            p2=p2.next
        return head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
#head.next.next.next.next=ListNode(5) 
c=Solution().oddEvenList(head)          
p=c
while p:
    print(p.val)
    p=p.next
            
            

