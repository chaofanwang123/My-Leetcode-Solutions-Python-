class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n==0 or n==1:
            return 0
        List=[]
        i=1
        while i<n:
            while i<n and prices[i]<=prices[i-1]:
                i+=1
            group=[prices[i-1]]
            while i<n and prices[i]>=prices[i-1]:
                i+=1
            group.append(prices[i-1])
            List.append(group)
        if List[-1][0]==List[-1][1]:
            del List[-1]
        n=len(List)
        summ=0
        for i in range(n):
            summ+=List[i][1]-List[i][0]
        return summ
prices=[1,2,3,4,5]
c=Solution().maxProfit(prices)