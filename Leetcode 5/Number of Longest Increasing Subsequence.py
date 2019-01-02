class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=0:
            return 0
        dp=[[1,1]]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j][0]>=dp[i][0]:
                        dp[i]=[dp[j][0]+1,dp[j][1]]
                    elif dp[j][0]==dp[i][0]-1:
                        dp[i][1]+=dp[j][1]
        maxl=0
        count=0
        for i in range(n):
            if dp[i][0]>maxl:
                maxl=dp[i][0]
                count=dp[i][1]
            elif dp[i][0]==maxl:
                count+=dp[i][1]
        return count
        
nums=[1,3,5,4,7]
c=Solution().findNumberOfLIS(nums)