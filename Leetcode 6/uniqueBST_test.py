class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
  def generateTrees(self, n):
    def newTree(x, l, r): 
      t = TreeNode(x)
      t.left = l
      t.right = r
      return t
    
    def gen(s, e):      
      return [newTree(i, l, r) for i in range(s, e + 1) for l in gen(s, i - 1) for r in gen(i + 1, e)] or [None]
        
    return gen(1, n) if n > 0 else []

c=Solution().generateTrees(5)