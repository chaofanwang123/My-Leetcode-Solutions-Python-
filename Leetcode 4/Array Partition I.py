class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)//2
        summ=0
        for i in range(n):
            summ+=nums[2*i]
        return summ

