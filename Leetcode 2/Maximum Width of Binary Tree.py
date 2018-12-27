class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        p=[[root,1]]
        q=[]
        maxl=0
        while p!=[]:
            maxl=max(maxl,p[-1][1]-p[0][1]+1)
            while p!=[]:
                node=p.pop(0)
                if node[0].left:
                    q.append([node[0].left,node[1]*2])
                if node[0].right:
                    q.append([node[0].right,node[1]*2+1])
            if q==[]:
                return maxl
            maxl=max(maxl,q[-1][1]-q[0][1]+1)
            while q!=[]:
                node=q.pop(0)
                if node[0].left:
                    p.append([node[0].left,node[1]*2])
                if node[0].right:
                    p.append([node[0].right,node[1]*2+1])
        return maxl

root=TreeNode(1)
root.left=TreeNode(3)
root.right=TreeNode(2)
root.left.left=TreeNode(5)
root.right.right=TreeNode(7)

c=Solution().widthOfBinaryTree(root)