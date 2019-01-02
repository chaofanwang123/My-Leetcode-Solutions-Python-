class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binarysearch(left,right):
            while left<=right:
                if nums[left]==target or nums[right]==target:
                    return True
                mid=(left+right)//2
                if nums[mid]==target:
                    return True
                if nums[mid]>target:
                    right=mid-1
                    left+=1
                else:
                    left=mid+1
                    right-=1
            return False
        left=0
        right=len(nums)-1
        while left<=right:
            if target==nums[left] or target==nums[right]:
                return True
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[right]:
                left+=1
                right-=1
                continue
            if target>nums[left]:
                if nums[mid]>target:
                    left+=1
                    right=mid-1
                    return binarysearch(left,right)
                elif nums[mid]>=nums[left]:
                    left=mid+1
                    right-=1
                else:
                    right=mid-1
                    left+=1
            else:
                if nums[mid]<target:
                    left=mid+1
                    right-=1
                    return binarysearch(left,right)
                elif nums[mid]<=nums[right]:
                    left+=1
                    right=mid-1
                else:
                    left=mid+1
                    right-=1
        return False
                    
nums = [2,5,6,0,0,1,2]
target = 3                
c=Solution().search(nums,target)
