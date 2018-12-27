class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        total=sum(nums)
        summ=0
        if summ==(total-nums[0])/2:
            return 0
        for i in range(1,len(nums)):
            summ+=nums[i-1]
            if summ==(total-nums[i])/2:
                return i
        return -1

