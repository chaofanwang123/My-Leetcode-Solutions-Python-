class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n=len(A)
        dp=[[0]*n for i in range(K)]
        summ=[0]*n
        summ[0]=A[0]
        for i in range(1,n):
            summ[i]=summ[i-1]+A[i]
        for i in range(n):
            dp[0][i]=summ[i]/(i+1)
        for i in range(1,K):
            dp[i][0]=A[0]
        for i in range(1,K):
            for j in range(1,n):
                if i>j:
                    dp[i][j]=summ[j]
                else:
                    dp[i][j]=dp[0][j]
                    for k in range(j):
                        dp[i][j]=max(dp[i][j],dp[i-1][k]+(summ[j]-summ[k])/(j-k))
        return dp[-1][-1]
        
A = [3]
K = 3
c=Solution().largestSumOfAverages(A,K)
