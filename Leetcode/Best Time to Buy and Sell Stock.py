class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        maxp=0
        minv=prices[0]
        n=len(prices)
        for i in range(1,n):
            maxp=max(maxp,prices[i]-minv)
            minv=min(minv,prices[i])
        return maxp

