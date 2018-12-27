class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[-1]
        left=0 
        right=n-1
        while left<right:
            if nums[left]<nums[right]:
                return nums[left]
            mid=(left+right)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if mid+1<n and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[right]<nums[right-1]:
                return nums[right]
            if nums[mid]>nums[left]:
                left=mid+1
                right-=1
            else:
                right=mid-1
                left+=1
        return nums[left]

nums=[1,2]
c=Solution().findMin(nums)