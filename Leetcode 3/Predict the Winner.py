class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n==1:
            return True
        dp=[[0]*n for i in range(n)]
        for j in range(n):
            dp[j][j]=nums[j]
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        return dp[0][n-1]>=0

nums=[1, 5, 2]
c=Solution().PredictTheWinner(nums)