# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def path(root,sum_value,d,target):
            count=0
            if root:
                sum_value+=root.val
                if sum_value-target in d:
                    count=d[sum_value-target]
                if sum_value in d:
                    d[sum_value]+=1
                else:
                    d[sum_value]=1
                count+=path(root.left,sum_value,d,target)+path(root.right,sum_value,d,target)
                d[sum_value]-=1
                return count
            return 0
        d=dict()
        d[0]=1
        return path(root,0,d,sum)

root=TreeNode(10)
root.left=TreeNode(5)
root.left.left=TreeNode(3)
root.left.right=TreeNode(2)
root.left.right.right=TreeNode(1)
root.left.left.left=TreeNode(3)
root.left.left.right=TreeNode(-2)
root.right=TreeNode(-3)
root.right.right=TreeNode(11)
sum=7
c=Solution().pathSum(root,sum)