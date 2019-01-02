class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length=1
        i=0
        n=len(nums)
        while i<n-1:
            count=1
            while i<n-1 and nums[i]<nums[i+1]:
                i+=1
                count+=1
            i+=1
            length=max(length,count)
        return length
                
        

