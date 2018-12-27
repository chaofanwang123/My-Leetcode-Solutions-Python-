class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        dp0,dp1=1,2
        for i in range(2,n):
            dp2=dp0+dp1
            dp0,dp1=dp1,dp2
        return dp1

