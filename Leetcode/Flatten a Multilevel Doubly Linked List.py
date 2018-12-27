# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(root):
            p=root
            while not p.child and p.next:
                p=p.next
            if p.child:
                if not p.next:
                    endroot=dfs(p.child)
                    p.child.pre=p
                    p.next=p.child
                    p.child=None
                    return endroot
                tmp=p.next
                endroot2=dfs(tmp)
                endroot=dfs(p.child)
                endroot.next=tmp
                endroot.next.pre=endroot
                p.child.pre=p
                p.next=p.child
                p.child=None
                return endroot2
            return p
        if not head:
            return head
        dfs(head)
        return head
            
head3=Node(11,None,None,None)
head3.next=Node(12,None,None,None)
head3.next.pre=head3
head2=Node(8,None,None,None)
head2.child=head3
head2.next=Node(9,None,None,None)
head2.next.pre=head2
head2.next.next=Node(10,None,None,None)
head2.next.next.pre=head2.next
head1=Node(3,None,None,None)
head1.child=Node(7,None,None,None)
head1.child.next=head2
head1.child.next.pre=head1.child
head1.next=Node(4,None,None,None)
head1.next.pre=head1
head1.next.next=Node(5,None,None,None)
head1.next.next.pre=head1.next          
head1.next.next.next=Node(6,None,None,None)
head1.next.next.next.pre=head1.next.next
head=Node(1,None,None,None)
head.next=Node(2,None,None,None)
head.next.pre=head
head.next.next=head1
head.next.next.pre=head.next

c=Solution().flatten(head)
while head.next:
    print(head.next.pre.val)
    head=head.next
            
#{"$id":"1","child":null,"next":{"$id":"2","child":null,"next":{"$id":"3","child":null,"next":{"$id":"4","child":null,"next":{"$id":"5","child":null,"next":{"$id":"6","child":null,"next":{"$id":"7","child":null,"next":{"$id":"8","child":null,"next":{"$id":"9","child":null,"next":{"$id":"10","child":null,"next":{"$id":"11","child":null,"next":{"$id":"12","child":null,"next":null,"prev":{"$ref":"11"},"val":6},"prev":{"$ref":"10"},"val":5},"prev":{"$ref":"3"},"val":4},"prev":{"$ref":"8"},"val":10},"prev":{"$ref":"5"},"val":9},"prev":{"$ref":"6"},"val":12},"prev":null,"val":11},"prev":{"$ref":"4"},"val":8},"prev":null,"val":7},"prev":{"$ref":"2"},"val":3},"prev":{"$ref":"1"},"val":2},"prev":null,"val":1}
#{"$id":"1","child":null,"next":{"$id":"2","child":null,"next":{"$id":"3","child":null,"next":{"$id":"4","child":null,"next":{"$id":"5","child":null,"next":{"$id":"6","child":null,"next":{"$id":"7","child":null,"next":{"$id":"8","child":null,"next":{"$id":"9","child":null,"next":{"$id":"10","child":null,"next":{"$id":"11","child":null,"next":{"$id":"12","child":null,"next":null,"prev":{"$ref":"11"},"val":6},"prev":{"$ref":"10"},"val":5},"prev":{"$ref":"9"},"val":4},"prev":{"$ref":"8"},"val":10},"prev":{"$ref":"7"},"val":9},"prev":{"$ref":"6"},"val":12},"prev":{"$ref":"5"},"val":11},"prev":{"$ref":"4"},"val":8},"prev":{"$ref":"3"},"val":7},"prev":{"$ref":"2"},"val":3},"prev":{"$ref":"1"},"val":2},"prev":null,"val":1}

     
