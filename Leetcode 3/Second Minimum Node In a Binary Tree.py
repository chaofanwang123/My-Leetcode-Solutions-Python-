# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def min2(root):
            if root.left==None:
                return [root.val]
            List=min2(root.left)+min2(root.right)
            List.sort()
            i=1
            while i<len(List) and List[i]==List[0]:
                i+=1
            if i==len(List):
                return List[0:2]
            return [List[0],List[i]]
        if not root:
            return -1
        List=min2(root)
        if List[0]==List[-1]:
            return -1
        return List[1]

root=TreeNode(2)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.right.left=TreeNode(5)
root.right.right=TreeNode(7)

c=Solution().findSecondMinimumValue(root)