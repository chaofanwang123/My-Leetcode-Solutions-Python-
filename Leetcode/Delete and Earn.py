class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        List=[]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                List.append([nums[i-1],count])
                count=1
        List.append([nums[-1],count])
        n=len(List)
        if n==1:
            return List[0][0]*List[0][1]
        dp=[0]*(n+1)
        dp[1]=List[0][0]*List[0][1]
        for i in range(2,n+1):
            if List[i-1][0]-1==List[i-2][0]:
                dp[i]=max(dp[i-1],dp[i-2]+List[i-1][0]*List[i-1][1])
            else:
                dp[i]=dp[i-1]+List[i-1][0]*List[i-1][1]
        return dp[-1]
        
        
                
nums = [3,1]
c=Solution().deleteAndEarn(nums)
