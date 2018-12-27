# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        if headA==headB:
            return headA
        p=headA
        m=1
        while p.next:
            p=p.next
            m+=1
        p=headB
        n=1
        while p.next:
            p=p.next
            n+=1
        p=headA
        q=headB
        if m>n:
            while m>n:
                m-=1
                p=p.next
        elif m<n:
            while n>m:
                n-=1
                q=q.next
        while p.next and p!=q:
            p=p.next
            q=q.next
        if p!=q:
            return None
        return p
        
                
        

headA=ListNode(3)
#headA.next=ListNode(2)
#headA.next.next=ListNode(3)
#headA.next.next.next=ListNode(4)
headB=ListNode(2)
headB.next=headA
#headB.next=ListNode(5)
#headB.next.next=headA.next.next
c=Solution().getIntersectionNode(headA,headB)
        
            
        
        

