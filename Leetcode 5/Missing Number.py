class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=i:
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
        for i in range(len(nums)):
            if nums[i]!=i:
                return i

nums=[9,6,4,2,3,5,7,0,1,10]
c=Solution().missingNumber(nums)