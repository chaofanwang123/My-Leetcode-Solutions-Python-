# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root and root.val==key:
            if root.left==None and root.right==None:
                root=None
            elif root.left==None:
                root=root.right
            elif root.right==None:
                root=root.left
            else:
                if root.left.left==None and root.left.right==None:
                    root.left.right=root.right
                    root=root.left
                elif root.left.right==None:
                    root.left.right=root.right
                    root=root.left
                else:    
                    p=root.left
                    while p.right:
                        p=p.right
                    tmp=p
                    p=None
                    tmp.right=root.right
                    tmp.left=root.left
                    root=tmp
            return root
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            root.left=self.deleteNode(root.left,key)
        return root

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)

c=Solution().deleteNode(root,3)                

