class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<2:
            return 0
        dp=[0]*n
        maxv=[0]*n
        maxv[0]=-prices[0]
        dp[1]=max(dp[0],prices[1]+maxv[0])
        maxv[1]=max(maxv[0],-prices[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],prices[i]+maxv[i-1])
            maxv[i]=max(maxv[i-1],-prices[i]+dp[i-2])
        return dp[-1]

prices=[1,2,3,0,2,0,9,7,10,4,13,2,6]
c=Solution().maxProfit(prices)