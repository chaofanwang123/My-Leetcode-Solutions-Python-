class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        n, ret, v, p = len(prices), 0, 0, 0
        profits, vp_pairs = [], []
        while p < n:
            v = p
            while v<n-1 and prices[v]>=prices[v+1]: v+=1
            p = v+1
            while p<n and prices[p] >= prices[p-1]: p+=1

            while (vp_pairs and prices[v] < prices[vp_pairs[-1][0]]):
                temp = vp_pairs.pop()
                profits.append(prices[temp[1]-1]-prices[temp[0]])

            while (vp_pairs and prices[p-1] >= prices[vp_pairs[-1][1]-1]):
                profits.append(prices[vp_pairs[-1][1]-1]-prices[v])
                v = vp_pairs.pop()[0]
            vp_pairs.append((v, p))

        while vp_pairs:
            temp = vp_pairs.pop()
            profits.append(prices[temp[1]-1]-prices[temp[0]])
            
        k = min(k, len(profits)) 
        profits.sort(key=lambda x: -x)
        for i in range(k):
            ret += profits[i]
        return ret   

prices=[3,2,6,5,0,3]
k = 2
c=Solution().maxProfit(k,prices)