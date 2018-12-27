class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        length=0
        while i<n:
            if nums[i]==1:
                j=i+1
                while j<n and nums[j]==1:
                    j+=1
                length=max(length,j-i)
                i=j+1
            else:
                i+=1
        return length
nums=[1,1,0,1,1,1]
c=Solution().findMaxConsecutiveOnes(nums)
