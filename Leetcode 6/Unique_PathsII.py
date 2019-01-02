class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m<1 or n<1 or obstacleGrid[0][0]==1:
            return 0
        p=obstacleGrid
        p[0][0]=1
        note=0
        for i in range(1,m):
            if obstacleGrid[i][0]==1 or note==1:
                note=1
                p[i][0]=0
            else:
                p[i][0]=1
        note=0
        for j in range(1,n):
            if obstacleGrid[0][j]==1 or note==1:
                note=1
                p[0][j]=0
            else:
                p[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    p[i][j]=0
                else:
                    p[i][j]=p[i-1][j]+p[i][j-1]
        return p[m-1][n-1]
                    
obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
c=Solution().uniquePathsWithObstacles(obstacleGrid)
