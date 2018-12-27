class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            if nums[i]<=0: nums[i]=n+2
        for i in range(n):
            if abs(nums[i])<=n:
                curr=abs(nums[i])-1
                nums[curr]=-abs(nums[curr])
        for i in range(n):
            if nums[i]>0: return i+1
        return n+1
        
nums=[3,4,-1,1]
c=Solution().firstMissingPositive(nums)
