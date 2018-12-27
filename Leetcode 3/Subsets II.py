class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        dp=set([])
        dp.add(())
        for i in range(n):
            temp=set()
            for item in dp:
                temp.add(tuple(list(item)+[nums[i]]))
            dp.update(temp)
        return [list(item) for item in dp]

nums=[4,4,4,1,4]
c=Solution().subsetsWithDup(nums)
