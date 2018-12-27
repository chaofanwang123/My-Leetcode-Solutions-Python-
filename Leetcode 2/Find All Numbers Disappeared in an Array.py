class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
        ans=[]
        for i in range(n):
            if nums[i]>0:
                ans.append(i+1)
        return ans

nums=[4,3,2,7,8,2,3,1]
c=Solution().findDisappearedNumbers(nums)