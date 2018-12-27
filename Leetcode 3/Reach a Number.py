import math
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        if target<=1:
            return target
        if target==2:
            return 3
        if target<=4:
            return target-1
        target=abs(target)
        n=(-1+math.sqrt(1+8*target))/2
        if n==int(n):
            return int(n)
        n=int(n)
        x=(n+2)*(n+1)//2-target
        x2=(n+3)*(n+2)//2-target
        if x%2==0:
            return n+1
        if x2%2==0:
            return n+2
        return n+3
        
c=Solution().reachNumber(7)
