class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]=dp[i]+dp[j-1]*dp[i-j]
        return dp[n]
    
c=Solution().numTrees(4)

