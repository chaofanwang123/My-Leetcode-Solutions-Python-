class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def nondecrease(arr):
            n=len(arr)
            if n==1 or n==0:
                return True
            i=1
            while i<n and arr[i]>=arr[i-1]:
                i+=1
            return True if i==n else False
        m=len(nums)
        if m<=2:
            return True
        i=1
        while i<m and nums[i]>=nums[i-1]:
            i+=1
        if i>=m-1:
            return True
        if nums[i+1]>=nums[i-1] and nondecrease(nums[i+1:]):
            return True
        if (i-2<0 or nums[i-2]<=nums[i]) and nondecrease(nums[i:]):
            return True
        return False
        
nums=[1,2,3,0,2,8]
c=Solution().checkPossibility(nums)          

