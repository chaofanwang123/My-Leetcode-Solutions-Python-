#class Solution:
#    def new21Game(self, N, K, W):
#        """
#        :type N: int
#        :type K: int
#        :type W: int
#        :rtype: float
#        """
#        if K==0:
#            return 1
#        if N-K+1>W:
#            return 1
#        dp=[0]*(K+1)
#        dp[0]=1
#        for i in range(1,K+1):
#            for j in range(1,W+1):
#                if i<=j:
#                    dp[i]+=1/W
#                else:
#                    dp[i]+=1/W*dp[i-j]
#        ans=dp[K]
#        for i in range(K+1,N+1):
#            for j in range(i-K+1,W+1):
#                if i<=j:
#                    ans+=1/W
#                else:
#                    ans+=1/W*dp[i-j]
#        return ans
N = 10
K = 1
W = 10
c=Solution().new21Game(N,K,W)            

