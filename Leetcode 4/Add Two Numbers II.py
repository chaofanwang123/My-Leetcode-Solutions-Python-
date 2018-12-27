# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
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
        l1=reverseList(l1)
        l2=reverseList(l2)
        p=l1
        q=l2
        overflow=0
        while q:
            p.val+=q.val+overflow
            if p.val<10:
                overflow=0
            else:
                overflow=1
                p.val=p.val%10
            if not p.next:
                break
            p=p.next
            q=q.next
        if not q:
            while p and overflow==1:
                p.val+=1
                if p.val<10:
                    break
                overflow=1
                p.val=0
                if not p.next:
                    p.next=ListNode(1)
                    break
                p=p.next     
            return reverseList(l1)
        if not q.next:
            if overflow==1:
                p.next=ListNode(1)
            return reverseList(l1)
        p.next=q.next
        p=p.next
        while p and overflow==1:
            p.val+=1
            if p.val<10:
                break
            overflow=1
            p.val=0
            if not p.next:
                p.next=ListNode(1)
                break
            p=p.next 
        return reverseList(l1)

l1=ListNode(7)
l1.next=ListNode(2)
l1.next.next=ListNode(4)
l1.next.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
p=Solution().addTwoNumbers(l1,l2)
while p:
    print(p.val)
    p=p.next            
            

