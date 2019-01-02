class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=2:
            return n
        i=0
        j=1
        while i+j<n:
            while i+j<n and nums[i+j]==nums[i]:
                if j==2:
                    del nums[i+j]
                    n-=1
                else:
                    j+=1
            i=i+j
            j=1
        return len(nums)
    
nums = [0,0,]
c=Solution().removeDuplicates(nums)
                

