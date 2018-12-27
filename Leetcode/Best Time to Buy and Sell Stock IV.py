class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        stack=[]
        if k==0:
            return 0
        n=len(prices)
        i=0
        while i<n-1:
            if prices[i]>=prices[i+1]:
                i+=1
                while i<n-1 and prices[i]>=prices[i+1]:
                    i+=1
            if i<n-1:
                start=prices[i]
                i+=1
                while i<n-1 and prices[i]<=prices[i+1]:
                    i+=1
                stack.append([start,prices[i]])
        if not stack:
            return 0
        i=len(stack)-1
        while i>0:
            if stack[i][0]>=stack[i-1][1]:
                stack[i-1][1]=stack[i][1]
                del stack[i]
            i-=1
        if len(stack)<=k:
            return sum(item[1]-item[0] for item in stack)
        List=[]
        for item in stack:
            List+=item
        dp=[[0 for j in range(k)] for i in range(len(stack))]
        for i in range(len(stack)):
            for j in range(k):
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])
                
        return

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= (n>>1):return self.maxProfit2(prices)
        dp =[[0 for j in range(n)]for i in range(k+1)]
 
        for i in xrange(1,k+1):
            maxTemp=-prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
                maxTemp =max(maxTemp,dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
 
    def maxProfit2(self,prices):
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans +=prices[i]-prices[i-1]
        return ans
