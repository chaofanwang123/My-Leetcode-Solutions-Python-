class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            if nums[0]<nums[1]:
                return 1
            return 0
        left=0
        right=n-1
        while left<=right:
            if left==right:
                return left
            if left==right-1:
                if nums[left]<nums[right]:
                    return right
                return left
            mid=(left+right)//2
            if nums[mid-1]>nums[mid]:
                right=mid-1
            elif nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                return mid
nums = [1,2,1,3,5,6,4]
c=Solution().findPeakElement(nums)                    

