# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        p=[]
        q=[]
        p.append(root)
        List=[root.val]
        while p!=[] or q!=[]:
            q=[]
            while p!=[]:
                node=p.pop()
                if node.right:
                    q.insert(0,node.right)
                if node.left:
                    q.insert(0,node.left)
            if q!=[]:
                List.append(q[-1].val)
            p=[]
            while q!=[]:
                node=q.pop()
                if node.right:
                    p.insert(0,node.right)
                if node.left:
                    p.insert(0,node.left)
            if p!=[]:
                List.append(p[-1].val)
        return List

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)

c=Solution().rightSideView(root)

