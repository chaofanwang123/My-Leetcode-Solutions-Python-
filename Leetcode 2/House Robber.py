class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        if n<=2:
            return max(nums)
        dp=[0]*n
        dp[0],dp[1]=nums[0],max(nums[1],nums[0])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

nums=[1,2,3,1]
c=Solution().rob(nums)