class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        min_nums=0
        sum_nums=nums[0]
        max_value=nums[0]
        for i in range(1,n):
            min_nums=min(min_nums,sum_nums)
            sum_nums+=nums[i]
            max_value=max(max_value,sum_nums-min_nums)
        return max_value

nums=[-2,1,-3,4,-1,2,1,-5,4]
c=Solution().maxSubArray(nums)

boggle=[['G','I','Z'],['U','E','K'],['Q','S','E']]