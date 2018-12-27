class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n=len(word1),len(word2)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(1,n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            dp[i][0]=i
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
        return dp[-1][-1]
word1 = ""
word2 = ''
c=Solution().minDistance(word1,word2)
