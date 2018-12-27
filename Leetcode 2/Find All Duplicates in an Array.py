class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[]
        for i in range(n):
            if nums[abs(nums[i])-1]<0:
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
        return ans

nums=[4,3,2,7,8,2,3,1]
c=Solution().findDuplicates(nums)