class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j,m,n):
            grid[i][j]=-1
            area=1
            if i+1<m and grid[i+1][j]==1:
                area+=dfs(i+1,j,m,n)
            if i-1>=0 and grid[i-1][j]==1:
                area+=dfs(i-1,j,m,n)
            if j+1<n and grid[i][j+1]==1:
                area+=dfs(i,j+1,m,n)
            if j-1>=0 and grid[i][j-1]==1:
                area+=dfs(i,j-1,m,n)
            return area
        m=len(grid)
        n=len(grid[0])
        area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=max(area,dfs(i,j,m,n))
        return area

