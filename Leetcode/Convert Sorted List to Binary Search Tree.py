# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        p1=p2=head
        while p2 and p2.next:
            p2=p2.next.next
            if p2==None or p2.next==None:
                break
            p1=p1.next
        root=TreeNode(p1.next.val)
        root.right=self.sortedListToBST(p1.next.next)
        p1.next=None
        root.left=self.sortedListToBST(head)
        return root
 
head=ListNode(-10)
head.next=ListNode(-3)
head.next.next=ListNode(0)
head.next.next.next=ListNode(5)
head.next.next.next.next=ListNode(9)
c=Solution().sortedListToBST(head)
        

