class Solution2:
    def maxProfit2(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        i=0
        high=None
        profit=0
        while i<n-1:
            if prices[i]>=prices[i+1]:
                i+=1
                while i<n-1 and prices[i]>=prices[i+1]:
                    i+=1
                if i<n-1:
                    low=prices[i]
                    i+=1
                    while i<n-1 and prices[i]<=prices[i+1]:
                        i+=1
                    if prices[i]-low>=fee:
                        if not high or high-low>=fee:
                            profit+=prices[i]-low-fee
                        else:
                            profit+=prices[i]-high
                        high=prices[i]
            else:
                low=prices[i]
                i+=1
                while i<n-1 and prices[i]<=prices[i+1]:
                    i+=1
                if prices[i]-low>=fee:
                    if not high or high-low>=fee:
                        profit+=prices[i]-low-fee
                    else:
                        profit+=prices[i]-high
                    high=prices[i]
        return profit

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2: 
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])
        return sell
class Solution3:
    def maxProfit3(self, prices, fee):
        buy = prices[0]
        res = 0
        for p in prices:
            if buy > p: # current price is less than last buy
                buy = p # buy at p
            else:
                tmp = p - buy - fee
                if tmp > 0: # have profit
                    res += tmp
                    buy = p - fee 
        return res
            
prices = [1, 3, 2, 8, 4, 9]
fee = 2               
c=Solution().maxProfit(prices,fee)
