class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n>=2:
            i=0
            while i<=n-2 and nums[n-1-i]<=nums[n-2-i]:
                i+=1
            if i==n-1:
                nums.reverse()    
            else:
                index=n-2-i
                i=0
                while nums[n-1-i]<=nums[index]:
                    i+=1
                index2=n-1-i
                nums[index],nums[index2]=nums[index2],nums[index]
                nums[index+1:]=sorted(nums[index+1:])
    
nums=[1,1]
c=Solution().nextPermutation(nums)

