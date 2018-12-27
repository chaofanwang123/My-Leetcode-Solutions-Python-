class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if i<0 or i>=m or j<0 or j>=n:
            return 1
        if min(i+1,m-i,j+1,n-j)>N:
            return 0
        return (self.findPaths(m,n,N-1,i-1,j)+self.findPaths(m,n,N-1,i+1,j)+self.findPaths(m,n,N-1,i,j-1)+self.findPaths(m,n,N-1,i,j+1))%(pow(10,9)+7)

class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp=[[0 for i1 in range(n+2)] for j1 in range(m+2)]
        for i1 in range(m+2):
            dp[i1][0]=1
            dp[i1][-1]=1
        for j1 in range(n+2):
            dp[0][j1]=1
            dp[-1][j1]=1
        
        for k in range(N):
            temp1=[[dp[i1][j1+1]+dp[i1+1][j1]+dp[i1+2][j1+1]+dp[i1+1][j1+2] for j1 in range(n)] for i1 in range(m)]
            for i1 in range(m):
                dp[i1+1]=[1]+temp1[i1]+[1]
        
        return dp[i+1][j+1]
                    
            
m = 10
n = 10
N = 9 
i = 5
j = 5
c=Solution().findPaths(m,n,N,i,j)