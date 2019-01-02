class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binarysearch(nums,l,r,target):
            if l<r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return True
                if nums[mid]>target:
                    return binarysearch(nums,l,mid-1,target)
                else:
                    return binarysearch(nums,mid+1,r,target)
            else:
                return nums[l]==target
        n=len(nums)
        if n==0:
            return False
        if target==nums[0]:
            return True
        if target<nums[0]:
            mid=(n-1)//2
            if nums[mid]<target:
                return binarysearch(nums,mid+1,n-1,target)
            elif nums[mid]>target:
                if nums[mid]
            return True        

nums = [2,5,6,0,0,1,2]
target = 5
c=Solution().search(nums,target)
