class Solution2:
    def knightProbability2(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def dfs(k,r,c):
            if k==0:
                return 1
            p=0
            for u,v in steps:
               if 0<=u+r<N and 0<=v+c<N:
                   p+=0.125*dfs(k-1,u+r,v+c)
            return p
        steps=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        return dfs(K,r,c)

class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K==0:
            return 1
        dp=[[1]*N for i in range(N)]
        steps=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        while K>0:
            K-=1
            temp=[[0]*N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    for u,v in steps:
                        if 0<=u+i<N and 0<=v+j<N:
                            temp[i][j]+=0.125*dp[u+i][v+j]
            dp=temp
        return dp[r][c]
        
N,K,r,c=10,13,5,3
c=Solution().knightProbability(N,K,r,c)
