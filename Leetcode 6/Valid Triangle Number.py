class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def twosides(List,side):
            m=len(List)
            left=0
            right=m-1
            count=0
            while left<right:
                while left<right and nums[left]+nums[right]<=side:
                    left+=1
                while left<right and nums[left]+nums[right]>side:
                    count+=right-left
                    right-=1
            return count
        nums.sort()
        n=len(nums)
        if n<3:
            return 0
        total=0
        for i in range(2,n):
            total+=twosides(nums[:i],nums[i])
        return total
nums=[2,2,2,3,4,5,2,4,8,9,2,5,3,2,7]
c=Solution().triangleNumber(nums)

