class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j,grid,m,n):
            grid[i][j]='*'
            if i+1<m and grid[i+1][j]=='1':
                dfs(i+1,j,grid,m,n)
            if i-1>=0 and grid[i-1][j]=='1':
                dfs(i-1,j,grid,m,n)
            if j+1<n and grid[i][j+1]=='1':
                dfs(i,j+1,grid,m,n)
            if j-1>=0 and grid[i][j-1]=='1':
                dfs(i,j-1,grid,m,n)
                
        if grid==[]:
            return 0
        count=0
        m=len(grid)
        n=len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j,grid,m,n)
                    count+=1
        return count

