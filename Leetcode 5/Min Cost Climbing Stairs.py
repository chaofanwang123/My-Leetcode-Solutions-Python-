class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp0=dp1=0
        for i in range(2,len(cost)+1):
            dp2=min(dp0+cost[i-2],dp1+cost[i-1])
            dp0,dp1=dp1,dp2
        return dp1
        
cost=[10,15,20]
c=Solution().minCostClimbingStairs(cost)
