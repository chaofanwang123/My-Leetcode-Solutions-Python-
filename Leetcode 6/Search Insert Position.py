class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left=0
        right=len(nums)-1
        if target<=nums[left]:
            return left
        if target==nums[right]:
            return right
        if target>nums[right]:
            return right+1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if nums[left]<target:
            return left+1
        return left

nums=[1,3,5,6]
target=0
c=Solution().searchInsert(nums,target)