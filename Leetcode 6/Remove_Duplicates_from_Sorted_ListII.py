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
        dummy=ListNode(float('inf'))
        dummy.next=head
        p=head
        start=dummy
        count=0
        while p:
            while p.next and p.next.val==start.next.val:
                p=p.next
                count+=1
            if count>0:
                start.next=p.next
                count=0
            else:
                start=p
            p=p.next
        return dummy.next  
        
head=ListNode(3)
head.next=ListNode(3)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(3)

c=Solution().deleteDuplicates(head)
p=c
while p:
    print(p.val)
    p=p.next

