# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        p=[]
        q=[]
        List=[]
        p.append(root)
        while p!=[] or q!=[]:
            l=[]
            while p!=[]:
                node=p.pop(0)
                l=l+[node.val]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l!=[]:
                List.append(l)
            l=[]
            while q!=[]:
                node=q.pop(0)
                l=[node.val]+l
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            if l!=[]:
                List.append(l)
        return List

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

c=Solution().zigzagLevelOrder(root)