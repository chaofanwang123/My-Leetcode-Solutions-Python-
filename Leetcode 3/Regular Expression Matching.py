class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for i in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]!='*':
                    dp[i][j]=dp[i-1][j-1] and (p[j-1]=='.' or p[j-1]==s[i-1])
                else:
                    if p[j-2]!='.':
                        if p[j-2]!=s[i-1]:
                            dp[i][j]=dp[i][j-2]
                        else:
                            k=i-1
                            while 0<=k and s[k]==s[i-1]:
                                if dp[k+1][j-2] or dp[k+1][j-1]:
                                    dp[i][j]=True
                                    break
                                k-=1
                            if k==-1:
                                dp[i][j]|=(dp[0][j-2] or dp[0][j-1])
                    else:
                        for k in range(i,-1,-1):
                            if dp[k][j-2]:
                                dp[i][j]=True
                                break
        return dp[-1][-1]

