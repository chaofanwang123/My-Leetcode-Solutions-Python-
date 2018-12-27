class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if n==1:
            return grid[0][0]==1
        dp=[[[0]*(n+1) for i in range(n+1)] for j in range(n+1)]
              
        for i in range(1,n+1):
            for j in range(1,n+1):
                for k in range(max(1,i+j-n),min(i+j-1,n)+1):
                    if grid[i-1][j-1]!=-1 or grid[k-1][i+j-k-1]!=-1:
                        dp[i][j][k]=max(dp[i-1][j][k-1],dp[i-1][j][k],dp[i][j-1][k-1],dp[i][j-1][k])
                        if k!=i:
                            dp[i][j][k]+=grid[i-1][j-1]+grid[k-1][i+j-k-1]
                        else:
                            dp[i][j][k]+=grid[i-1][j-1]
        return dp[n][n][n]

grid =[[1,1,-1],[1,-1,1],[-1,1,1]]    
c=Solution().cherryPickup(grid) 
                        