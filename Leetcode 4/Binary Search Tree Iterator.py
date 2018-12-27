# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val
    
    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

root=TreeNode(1)
root.right=TreeNode(5)
root.right.left=TreeNode(3)

c= BSTIterator(root)
if c.hasNext():
    m=c.next()

