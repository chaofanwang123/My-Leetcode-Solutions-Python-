class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        res = 0
        dp = [[0 for i in range(N)] for j in range(N)]
        s = set()
        for mine in mines:
            s.add(tuple(mine))
        for i in range(N):
            cnt = 0
            for j in range(N):
                cnt = 0 if (i,j) in s else cnt + 1
                dp[i][j] = cnt
            cnt = 0
            for j in range(N - 1, -1, -1):
                cnt = 0 if (i,j) in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
        for j in range(N):
            cnt = 0
            for i in range(N):
                cnt = 0 if (i,j) in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for i in range(N - 1, -1, -1):
                cnt = 0 if (i,j) in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
                res = max(dp[i][j], res)
        return res