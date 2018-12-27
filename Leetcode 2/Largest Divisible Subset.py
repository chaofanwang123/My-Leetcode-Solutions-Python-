class Solution2:
    def largestDivisibleSubset2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n==0 or n==1:
            return []
        nums.sort()
        dp=[1]*n
        stack=[[]]*n
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    stack[i]=stack[j].append(nums[i])
        maxv=dp[0]
        ans=stack[0]
        for i in range(1,n):
            if dp[i]>maxv:
                maxv=dp[i]
                ans=stack[i]
        return ans
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        pre = [None] * n
        for x in range(n):
            for y in range(x):
                if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
                    dp[x] = dp[y] + 1
                    pre[x] = y
        idx = dp.index(max(dp))
        ans = []
        while idx is not None:
            ans += nums[idx],
            idx = pre[idx]
        return ans
                
nums=[1,2,3]
c=Solution().largestDivisibleSubset(nums)
