# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [root]*k
        n=1
        p=root
        while p.next:
            p=p.next
            n+=1
        length,rem=n//k,n%k
        ans=[[]]*k
        p=root
        for i in range(rem):
            start=p
            for j in range(length):
                p=p.next
            tmp=p
            p=p.next
            tmp.next=None
            ans[i]=start
        if length==0:
            return ans
        for i in range(rem,k):
            start=p
            for j in range(length-1):
                p=p.next
            tmp=p
            p=p.next
            tmp.next=None
            ans[i]=start
        return ans

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
#l1.next.next.next.next=ListNode(5)
k=5
c=Solution().splitListToParts(l1,k)            
                
                

