class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)
        if total%2:
            return False
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for i in nums:
            if target<i:
                return False
            if dp[target-i]:
                return True
            for j in range(target-i,-1,-1):
                if dp[j]:
                    dp[j+i]=True
        return dp[-1]
            
nums=[1,2,5]
c=Solution().canPartition(nums)        
