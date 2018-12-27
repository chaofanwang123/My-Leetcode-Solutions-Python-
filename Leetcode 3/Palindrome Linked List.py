# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
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
        
        if not head or not head.next:
            return True
        dummy=ListNode(0)
        dummy.next=head
        p1=dummy
        p2=head
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
        head2=p1.next.next
        if p2.next:
            p1.next.next=None
        else:
            p1.next=None
        head=reverse(head)
        p1=head
        p2=head2
        while p1.val==p2.val and p1.next and p2.next:
            p1=p1.next
            p2=p2.next
        if p1.val!=p2.val:
            return False
        return True

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(1)
c=Solution().isPalindrome(head)
