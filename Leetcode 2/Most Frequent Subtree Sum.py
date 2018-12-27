# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root:
                if root in memo:
                    return memo[root]
                sum1,sum2=0,0
                if root.left:
                    sum1=helper(root.left)
                if root.right:
                    sum2=helper(root.right)
                summ=sum1+sum2+root.val
                memo[root]=summ
                d[summ]+=1
                return summ
        
        if not root:
            return []
        d=defaultdict(int)
        memo={}
        helper(root)
        maxcount=max(d.values())
        ans=[]
        for key in d:
            if d[key]==maxcount:
                ans.append(key)
        return ans

root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(-3)
c=Solution().findFrequentTreeSum(root)