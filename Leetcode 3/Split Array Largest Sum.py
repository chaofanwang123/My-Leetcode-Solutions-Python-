class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n=len(nums)
        dp=[[float('inf')]*n for i in range(m)]
        summ=[0]*(n+1)
        for i in range(n-1,-1,-1):
            summ[i]=summ[i+1]+nums[i]
        for j in range(n):
            dp[0][j]=summ[0]-summ[j+1]
        for i in range(1,m):
            for j in range(i,n):
                for k in range(i-1,j):
                    dp[i][j]=min(dp[i][j],max(dp[i-1][k],summ[k+1]-summ[j+1]))
        return dp[-1][-1]

class Solution2:
    def splitArray2(self, nums, m): 
        N = len(nums)
        if N==m: return max(nums)
        low, high = max(nums), sum(nums)
        
        while low <= high:
            mid = (low + high)//2
            count, cum = 1, 0
            for num in nums:
                if cum + num <= mid: cum+=num
                else:
                    count+=1
                    cum = num
                    if count > m: break
            if count <= m: high = mid-1
            else: low = mid+1
        return low
    
nums = [7]
m = 1
c=Solution2().splitArray2(nums,m)