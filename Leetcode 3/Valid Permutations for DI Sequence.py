class Solution:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        n=len(S)
        dp=[[0]*(n+1) for i in range(n+1)] # dp[i][k]=# of sub when P[i]=k
        dp[0][0]=1
        for i in range(1,n+1):
            if S[i-1]=='D':
                dp[i][i-1]=dp[i-1][i-1]
                for k in range(i-2,-1,-1):
                    dp[i][k]=dp[i][k+1]+dp[i-1][k]
            else:
                dp[i][1]=dp[i-1][0]
                for k in range(1,i):
                    dp[i][k+1]=dp[i][k]+dp[i-1][k]
        return sum(dp[n][j] for j in range(n+1))%(pow(10,9)+7)
        
S='D'
c=Solution().numPermsDISequence(S)