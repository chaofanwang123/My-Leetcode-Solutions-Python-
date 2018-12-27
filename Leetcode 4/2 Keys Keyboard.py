class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=i
            for j in range(i//2,0,-1):
                if i%j==0:
                    dp[i]=min(dp[i],dp[j]+i//j)
        return dp[-1]

