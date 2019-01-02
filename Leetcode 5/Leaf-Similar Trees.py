# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stack1=[root1]
        stack2=[root2]
        while stack1!=[] and stack2!=[]:
            value1=-1000
            while stack1!=[]:
                p=stack1.pop(0)
                if not p.left and not p.right:
                    value1=p.val
                    break
                else:
                    if p.right:
                        stack1.insert(0,p.right)
                    if p.left:
                        stack1.insert(0,p.left)
            value2=-1001
            while stack2!=[]:
                p=stack2.pop(0)
                if not p.left and not p.right:
                    value2=p.val
                    break
                else:
                    if p.right:
                        stack2.insert(0,p.right)
                    if p.left:
                        stack2.insert(0,p.left)
            if value1!=value2:
                return False
        if stack1==[] and stack2==[]:
            return True
        return False
                

