class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        m,n=len(dungeon),len(dungeon[0])
        dp=[[0]*n for i in range(m)]
        dp[m-1][n-1]=max(1-dungeon[m-1][n-1],1)
        for i in range(m-2,-1,-1):
            dp[i][n-1]=max(dp[i+1][n-1]-dungeon[i][n-1],1)
        for j in range(n-2,-1,-1):
            dp[m-1][j]=max(dp[m-1][j+1]-dungeon[m-1][j],1)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]

dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
c=Solution().calculateMinimumHP(dungeon)

