class Solution2:
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

import bisect
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        List=[nums[0]]
        for i in range(1,n):
            if nums[i]>List[-1]:
                List.append(nums[i])
            elif nums[i]<List[-1]:
                index=bisect.bisect_left(List,nums[i])
                List[index]=nums[i]
        return len(List)
        
        
nums=[2,2]
c=Solution().lengthOfLIS(nums)