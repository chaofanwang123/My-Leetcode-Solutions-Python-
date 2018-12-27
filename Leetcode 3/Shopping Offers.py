class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def dfs(price,special,needs,n,cost):
            if needs==[0]*n:
                self.min=min(self.min,cost)
                return
            count=0
            for item in special:
                j=0
                while j<n and needs[j]>=item[j]:
                    j+=1
                if j==n:
                    count+=1
                    dfs(price,special,[needs[k]-item[k] for k in range(n)],n,cost+item[-1])
            if count==0:
                for i in range(n):
                    cost+=price[i]*needs[i]
                self.min=min(self.min,cost)
                return
        
        m=len(special)
        n=len(needs)
        i=m-1
        while i>=0:
            cost=0
            for j in range(n):
                cost+=price[j]*special[i][j]
            if cost<=special[i][-1]:
                del special[i]
            i-=1   
        self.min=float('inf')
        dfs(price,special,needs,n,0)
        return self.min

price=[2,5]
special=[[3,0,5],[1,2,10]]
needs=[3,2]

c=Solution().shoppingOffers(price,special,needs)

