class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 0
        min2=[0]*n
        max1=[0]*n
        max1[0]=nums[0]
        min2[n-1]=nums[n-1]
        for i in range(1,n):
            max1[i]=max(max1[i-1],nums[i])
            min2[n-1-i]=min(min2[n-i],nums[n-1-i])
        
        i=0
        while i<n and max1[i]<=min2[i]:
            i+=1
        j=n-1
        while j>0 and max1[j]<=min2[j]:
            j-=1
        return max(j-i+1,0)
            
nums=[2, 6, 4, 8, 10, 9, 15,3]
c=Solution().findUnsortedSubarray(nums)
