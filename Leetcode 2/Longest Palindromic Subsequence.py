class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n=len(s)
        if n==1:
            return 1
        dp=[[0]*n for i in range(n)]
        for j in range(n):
            dp[j][j]=1
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if s[i]!=s[j]:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
                else:
                    dp[i][j]=dp[i+1][j-1]+2 if i+1<=j-1 else 2
        return dp[0][n-1]

s="cbbd"
c=Solution().longestPalindromeSubseq(s)