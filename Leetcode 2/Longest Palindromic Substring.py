class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<=1:
            return s
        dp=[[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=True
        maxl=1
        maxs=s[0]
        for j in range(1,n):
            for i in range(j):
                if s[i]==s[j] and (i+1==j or dp[i+1][j-1]):
                    dp[i][j]=True
                    if j-i+1>maxl:
                        maxl=j-i+1
                        maxs=s[i:j+1]
        return maxs

