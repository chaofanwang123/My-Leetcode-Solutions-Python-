class Solution2:
    def soupServings2(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N==0:
            return 0.5
        if N%25==0:
            N=N//25
        else:
            N=N//25+1
        dp1=[[0]*(N+1) for i in range(N+1)] # prob of A empty first
        dp2=[[0]*(N+1) for i in range(N+1)] #prob of A and B empty at the same time
        dp1[0]=[0]+[1]*N
        dp2[0][0]=1
        opr=[[4,0],[3,1],[2,2],[1,3]]
        for i in range(1,N+1):
            for j in range(1,N+1):
                for u,v in opr:
                    if i-u<=0:
                        if j-v>0:
                            dp1[i][j]+=0.25*dp1[0][j-v]
                        else:
                            dp2[i][j]+=0.25*dp2[0][0]
                    elif j-v>0:
                        dp1[i][j]+=0.25*dp1[i-u][j-v]
                        dp2[i][j]+=0.25*dp2[i-u][j-v]
        return dp1[N][N]+0.5*dp2[i][j]

class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        def helper(x,y):
            if x<=0 and y<=0:
                return 0.5
            if x<=0:
                return 1
            if y<=0:
                return 0
            if (x,y) in memo:
                return memo[(x,y)]
            ans=0.25*(helper(x-100,y)+helper(x-75,y-25)+helper(x-50,y-50)+helper(x-25,y-75))
            memo[(x,y)]=ans
            return ans
        memo = {}
        if N >= 14000: 
            return 1
        return helper(N, N)
    
c=Solution().soupServings(2500)                      
        
