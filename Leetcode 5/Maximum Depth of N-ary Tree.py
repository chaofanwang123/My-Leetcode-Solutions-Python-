class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        length=0
        for child in root.children:
            length=max(self.maxDepth(child),length)
        return length+1
                
        
        

