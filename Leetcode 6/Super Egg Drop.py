class Solution2:
    def superEggDrop2(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if K==1:
            return N
        dp=[[0]*K for i in range(N+1)]
        for i in range(N+1):
            dp[i][0]=i
        for j in range(K):
            dp[1][j]=1
        for i in range(2,N+1):
            dp[i][1]=dp[i-1][1]+1
            for k in range(2,i+1):
                dp[i][1]=min(dp[i][1],max(dp[k-1][0],dp[i-k][1])+1)
        for i in range(2,N+1):
            for j in range(2,K):
                dp[i][j]=max(dp[0][j-1],dp[i-1][j])+1
                for k in range(2,i+1):
                    dp[i][j]=min(dp[i][j],max(dp[k-1][j-1],dp[i-k][j])+1)
        return dp[N][K-1]

class Solution:
    def superEggDrop(self, K, N):
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            for k in range(K, 0, -1):
                dp[k] = dp[k - 1] + dp[k] + 1
            m += 1
        return m

K=3
N=10
c=Solution().superEggDrop(K,N)