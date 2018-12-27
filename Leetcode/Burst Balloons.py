class Solution:
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for k in range(2, n): 
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n - 1]
            

