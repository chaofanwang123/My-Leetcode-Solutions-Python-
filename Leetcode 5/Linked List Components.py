# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import defaultdict
class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        d1=defaultdict(list)
        d2=defaultdict(list)
        p=head
        while p.next:
            d1[p.val]=p.next.val
            d2[p.next.val]=p.val
            p=p.next
        G=set(G)
        count=0
        while G:
            node=G.pop()
            temp=node
            temp2=node
            while temp in d1 and d1[temp] in G:
                G.remove(d1[temp])
                temp=d1[temp]
            while temp2 in d2 and d2[temp2] in G:
                G.remove(d2[temp2])
                temp2=d2[temp2]
            count+=1
        return count
                    
head=ListNode(0)
head.next=ListNode(1)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(4)
G=[0,1,2,3,4]
c=Solution().numComponents(head,G)

