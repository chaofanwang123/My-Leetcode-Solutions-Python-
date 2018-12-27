class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0.0] * N
        summ = 1.0000
        for i in range(1, N + 1):
            dp[i] = summ / W
            if i < K: 
                summ += dp[i]
            if 0 <= i - W < K: 
                summ -= dp[i - W]
        return sum(dp[K:])
        

