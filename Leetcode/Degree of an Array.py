from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        length=50000
        degree=0
        for item in d:
            if len(d[item])>degree:
                degree=len(d[item])
                length=d[item][-1]-d[item][0]+1
            elif len(d[item])==degree:
                length=min(length,d[item][-1]-d[item][0]+1)
        return length

