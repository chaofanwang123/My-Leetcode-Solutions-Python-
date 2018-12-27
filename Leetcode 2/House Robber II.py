class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        if n<=3:
            return max(nums)
        dp=[0]*(n-1)
        # if don't break 0
        dp[0],dp[1]=nums[1],max(nums[1],nums[2])
        for i in range(2,n-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i+1])
        maxv=dp[-1]
        # if break 0
        dp[0],dp[1]=nums[2],max(nums[2],nums[3])
        for i in range(2,n-3):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i+2])
        return max(maxv,dp[n-4]+nums[0])

