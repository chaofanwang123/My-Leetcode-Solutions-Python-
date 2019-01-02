class Solution:
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for x in range(m)]
        ans = 0
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])
                if x and y and dp[x][y]:
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
                ans = max(ans, dp[x][y])
        return ans * ans

