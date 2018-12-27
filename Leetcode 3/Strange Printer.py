from collections import defaultdict
class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0 or n==1:
            return n
        i=1
        s=s+'#'
        List=[s[0]]
        while s[i]!='#':
            if s[i]==s[i-1]:
                s=s[:i]+s[i+1:]
            else:
                List.append(s[i])
                i+=1
        n=len(List)
        if n==1:
            return 1
        dp=[[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i]=1
        for j in range(n):
            for i in range(j):
                dp[i][j]=float('inf')
                if s[i]==s[j]:
                    dp[i][j]=min(dp[i][j],dp[i][j-1])
                else:
                    dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
                for k in range(i+1,j):
                    if s[k]==s[j]:
                        dp[i][j]=min(dp[i][j],dp[i][k-1]+dp[k][j-1])
                    else:
                        dp[i][j]=min(dp[i][j],dp[i][k-1]+dp[k][j-1]+1)
        return dp[0][n-1]
                
#class Solution(object):
#    def strangePrinter(self, s):
#        if not s:
#            return 0
#        #reduce the input
#        fs = s[0]
#        for i in range(1, len(s)):
#            if s[i] != s[i - 1]:
#                fs += s[i]
#        l = len(fs)
#        dp = [[0xffffffff for i in range(l)] for j in range(l)]
#        for i in range(l):
#            dp[i][i] = 1
#        for i in range(l):
#            for j in range(i - 1, -1, -1):
#                if fs[i] == fs[j]:
#                    dp[i][j] = min(dp[i - 1][j + 1] + 1, dp[i - 1][j], dp[i][j + 1])
#                else:
#                    for x in range(j + 1, i + 1):
#                        dp[i][j] = min(dp[i][x] + dp[x - 1][j], dp[i][j])
#        return dp[-1][0]
            
        
        
s="aba"
c=Solution().strangePrinter(s)
                

