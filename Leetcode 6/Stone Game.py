class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n=len(piles)
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=piles[i]
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                dp[i][j]=max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
        return dp[0][n-1]>0
    

