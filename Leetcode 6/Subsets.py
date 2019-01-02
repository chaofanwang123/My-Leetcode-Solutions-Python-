class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        dp=[[]]
        n=len(nums)
        for i in range(n):
            temp=[item+[nums[i]] for item in dp]
            dp+=temp
        return dp
nums=[1,2,3]
c=Solution().subsets(nums)

