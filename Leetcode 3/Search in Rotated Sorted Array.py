class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        if n==0: return -1
        if n==1: 
            if nums[0]==target:
                return 0
            return -1
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target: 
                return mid
            elif nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            else:
                if nums[mid]>=nums[left]:
                    if nums[left]<target<nums[mid]:
                        left+=1
                        right=mid-1
                    else:
                        left=mid+1
                        right-=1
                else:
                    if nums[right]>target>nums[mid]:
                        left=mid+1
                        right-=1
                    else:
                        left+=1
                        right=mid-1
        return -1
