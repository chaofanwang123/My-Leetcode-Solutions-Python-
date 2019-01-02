class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        count=0
        n=len(nums)
        while i<n-count:
            if nums[i]==0:
                nums[i:n-count-1],nums[n-count-1]=nums[i+1:n-count],nums[i]
                count+=1
            else:
                i+=1

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[index] = nums[i]
                index = index + 1
        for i in range(index, len(nums)):
            nums[i] = 0
            
nums=[0,0,1]
c=Solution().moveZeroes(nums)