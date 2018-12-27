class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        n=len(S)
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=1
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if S[i]!=S[j]:
                    dp[i][j]=dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                else:
                    if i+1==j:
                        dp[i][j]=2
                    else:
                        index=S[i+1:j].find(S[i])
                        if index==-1:
                            dp[i][j]=2*dp[i+1][j-1]+2
                        else:
                            index2=S[i+1:j].rfind(S[i])
                            if index==index2:
                                dp[i][j]=2*dp[i+1][j-1]+1
                            else:
                                dp[i][j]=2*dp[i+1][j-1]-dp[index+i+2][index2+i]
        return dp[0][n-1]%(10**9+7)
S = 'aba'
c=Solution().countPalindromicSubsequences(S)
