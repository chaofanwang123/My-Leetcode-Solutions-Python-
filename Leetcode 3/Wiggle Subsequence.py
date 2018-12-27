class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<2:
            return n
        dp1=[0]*n
        dp2=[0]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp1[i]=max(dp1[i],dp2[j]+1)
                elif nums[i]<nums[j]:
                    dp2[i]=max(dp2[i],dp1[j]+1)
        return 1+max(max(dp1),max(dp2))

nums=[1,2,3,4,5,6,7,8,9]
c=Solution().wiggleMaxLength(nums)