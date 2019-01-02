# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseNode(start,end):
            p=start.next
            while start.next!=end:
                tmp=p.next
                p.next=tmp.next
                tmp.next=start.next
                start.next=tmp
            return p
        if k==0 or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        start=dummy
        count=0
        while p.next:
            count+=1
            p=p.next
            if count==k:
                temp=p.next
                new_end=reverseNode(start,p)
                new_end.next=temp
                start=new_end
                p=new_end
                count=0
        return dummy.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)

c=Solution().reverseKGroup(head,7)
#c2=reverseNode(head.next,head.next.next.next.next)
p=c
while p:
    print(p.val)
    p=p.next
        

