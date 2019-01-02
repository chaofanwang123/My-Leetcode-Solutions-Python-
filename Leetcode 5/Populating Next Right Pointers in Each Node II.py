# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            if root.right:
                root.left.next=root.right
                p=root.next
                while p:
                    if p.left:
                        root.right.next=p.left
                        break
                    if p.right:
                        root.right.next=p.right
                        break
                    p=p.next
                self.connect(root.right)
                self.connect(root.left)
            else:
                p=root.next
                while p:
                    if p.left:
                        root.left.next=p.left
                        break
                    if p.right:
                        root.left.next=p.right
                        break
                    p=p.next
                self.connect(root.left)
        elif root.right:
            p=root.next
            while p:
                if p.left:
                    root.right.next=p.left
                    break
                if p.right:
                    root.right.next=p.right
                    break
                p=p.next
                self.connect(root.right)
    
root=TreeLinkNode(-9)
root.left=TreeLinkNode(-3)
root.right=TreeLinkNode(2) 
root.left.left=TreeLinkNode(4)
root.left.right=TreeLinkNode(5)     
root.right.right=TreeLinkNode(7)

Solution().connect(root)            
            

