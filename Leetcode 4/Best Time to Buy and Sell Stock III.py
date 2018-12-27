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
        if n==0:
            return 0
        if n==1:
            return List[0][1]-List[0][0]
        dp1=[0]*n
        dp2=[0]*n
        dp1[0]=List[0][1]-List[0][0]
        dp2[n-1]=List[n-1][1]-List[n-1][0]
        min1=List[0][0]
        max2=List[n-1][1]
        for i in range(1,n):
            min1=min(min1,List[i][0])
            dp1[i]=max(dp1[i-1],List[i][1]-min1)
            max2=max(max2,List[n-1-i][1])
            dp2[n-1-i]=max(dp2[n-i],max2-List[n-1-i][0])
        maxv=dp1[0]+dp2[1]
        for i in range(1,n-1):
            maxv=max(maxv,dp1[i]+dp2[i+1])
        return maxv
prices=[7,6,4,3,1]
c=Solution().maxProfit(prices)
            

