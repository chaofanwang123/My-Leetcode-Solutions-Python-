"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        p=[root]
        q=[]
        ans=[]
        while p:
            value=[]
            while p:
                node=p.pop(0)
                value.append(node.val)
                q+=node.children
            ans.append(value)
            if not q:
                return ans
            value=[]
            while q:
                node=q.pop(0)
                value.append(node.val)
                p+=node.children
            ans.append(value)
        return ans

