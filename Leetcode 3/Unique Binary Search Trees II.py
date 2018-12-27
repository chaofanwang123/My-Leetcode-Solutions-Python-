# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def gentree(m,offset):
            if m==0:
                return None
            if m==1:
                return [TreeNode(1+offset)]
            List=[]
            for i in range(1,m+1):
                left=gentree(i-1,offset)
                right=gentree(m-i,offset+i)
                if left==None:
                    for j in right:
                        root=TreeNode(i+offset)
                        root.right=j
                        List.append(root)
                elif right==None:
                    for j in left:
                        root=TreeNode(i+offset)
                        root.left=j
                        List.append(root)
                else:
                    for j in left:
                        for k in right:
                            root=TreeNode(i+offset)
                            root.left=j
                            root.right=k
                            List.append(root)
            return List
        if n==0:
            return []
        return gentree(n,0)

