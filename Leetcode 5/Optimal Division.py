class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n=len(nums)
        if n==1:
            return str(nums[0])
        if n==2:
            return str(nums[0])+'/'+str(nums[1])
        s=''
        for i in range(1,n):
            s+='/'+str(nums[i])
        return str(nums[0])+'/'+'('+s[1:]+')'

nums=[1000,100,10,2]
c=Solution().optimalDivision(nums)