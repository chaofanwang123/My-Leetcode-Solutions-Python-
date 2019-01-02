class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:return 1
        if n==3: return 2
        dp=[1]*(n+1)
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=max(dp[i],dp[j]*(i-j))
        return dp[-1]

c=Solution().integerBreak(4)