# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        p=[root]
        q=[]
        List=[]
        while p!=[]:
            summ=0
            n=len(p)
            while p!=[]:
                node=p.pop(0)
                summ+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            List.append(summ/n)
            if q==[]:
                return List
            summ=0
            n=len(q)
            while q!=[]:
                node=q.pop(0)
                summ+=node.val
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            List.append(summ/n)
            if p==[]:
                return List

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

c=Solution().averageOfLevels(root)