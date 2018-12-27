# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        table = {}
        res = set()
        def util(node):
            if not node:
                return '#'
            l = util(node.left)
            r = util(node.right)
            k = (l, node.val ,r)
            if k in table:
                res.add(table[k])
            else:
                table[k] = node
            return table[k]
        util(root)
        return list(res)
    def findDuplicateSubtrees2(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def sameroot(root1,root2):
            if root1==None:
                return root2==None
            if root2==None:
                return root1==None
            return root1.val==root2.val and sameroot(root1.left,root2.left) and sameroot(root1.right,root2.right)
        def duptree(root):
            if not root:
                return []
            if root:
                l=duptree(root.left)
                r=duptree(root.right)
                if l==[] or r==[]:
                    return l+r+[root]
                i=0
                while i<len(l):
                    j=0
                    while j<len(r) and sameroot(l[i],r[j])==False:
                        j+=1
                    if j!=len(r):
                        # check if l[i] in self.List
                        length=len(self.List)
                        k=0
                        while k<length:
                            if sameroot(l[i],self.List[k]):
                                break
                            k+=1
                        if k==length:
                            self.List.append(l[i])
                        del r[j]
                        del l[i]
                    else:
                        i+=1
                return r+l+[root]
        self.List=[]
        duptree(root)
        return self.List

root=TreeNode(0)
root.left=TreeNode(0)
root.right=TreeNode(0)
root.left.left=TreeNode(0)
root.right.right=TreeNode(0)
root.left.left.left=TreeNode(0)
root.left.left.right=TreeNode(0)
root.right.right.left=TreeNode(0)
root.right.right.right=TreeNode(0)

c=Solution().findDuplicateSubtrees(root)