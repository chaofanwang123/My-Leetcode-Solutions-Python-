class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i=len(nums)-1
        while i>0:
            if nums[i-1]==nums[i]:
                del nums[i-1]
            i-=1
        return len(nums)

nums=[1,1]
c=Solution().removeDuplicates(nums)