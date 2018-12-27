class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for L in range(n - 1, 0, -1):
            for R in range(L + 1, n + 1):
                dp[L][R] = min(i + max(dp[L][i - 1], dp[i + 1][R]) for i in range(L, R))
        return dp[1][n]

#class Solution2:
#    def getMoneyAmount2(self, n):
#        """
#        :type n: int
#        :rtype: int
#        """
#        if n==1:
#            return 0
#        if n==2:
#            return 1
#
#        dp=[n**2]*(n+1)
#        dp[0]=0
#        dp[1]=0
#        dp[2]=1
#        times=[0]*n
#        i=1
#        factor=2
#        while i<n:
#            if i<factor:
#                times[i]=times[i-1]
#            else:
#                factor*=2
#                times[i]=times[i-1]+1
#            i+=1
#        
#        for i in range(3,n+1):
#            for j in range(i//2+1,i):
#                temp=j+max(dp[j-1],dp[i-j]+times[i-j]*j)
#                if temp<dp[i]:
#                    dp[i]=temp
#        return dp[-1]

n=50
c=Solution().getMoneyAmount(n)