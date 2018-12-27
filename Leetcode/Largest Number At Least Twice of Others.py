class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value=-float('inf')
        for i in range(len(nums)):
            if nums[i]>value:
                value=nums[i]
                index=i
        for i in range(len(nums)):
            if i!=index and 2*nums[i]>value:
                return -1
        return index
        

