# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        p=head       
        while p:
            node=RandomListNode(p.label)
            node.next=p.next
            p.next=node
            p=node.next
        q=head
        while q:
            if q.random:
                q.next.random=q.random.next
            q=q.next.next
        p=head
        head2=head.next
        q=head.next
        while q.next:
            p.next=q.next
            p=p.next
            q.next=p.next
            q=q.next
        p.next=None
        q.next=None
        return head2
    def copyRandomList2(self, head):
        if head == None: return None
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead

head=RandomListNode(1)
head.next=RandomListNode(2)
head.next.next=RandomListNode(3)
head.next.next.next=RandomListNode(4)

head.random=head.next.next
head.next.random=head
head.next.next.random=head.next
head.next.next.next.random=head.next

p=head
while p.next:
    print([p.label],[p.next.label],[p.random.label])
    p=p.next
print([p.label],None,[p.random.label])
#head2=RandomListNode(-1)
c=Solution().copyRandomList(head)

print('copied list:\n')
p=c
while p.next:
    print([p.label],[p.next.label],[p.random.label])     
    p=p.next
print([p.label],None,[p.random.label])
