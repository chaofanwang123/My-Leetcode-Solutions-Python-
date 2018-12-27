class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j,limit):
            if i==N-1 and j==N-1:
                return True
            visited[i][j]=True
            if i+1<N and not visited[i+1][j] and grid[i+1][j]<=limit:
                if dfs(i+1,j,limit):
                    return True
            if i-1>=0 and not visited[i-1][j] and grid[i-1][j]<=limit:
                if dfs(i-1,j,limit):
                    return True
            if j+1<N and not visited[i][j+1] and grid[i][j+1]<=limit:
                if dfs(i,j+1,limit):
                    return True
            if j-1>=0 and not visited[i][j-1] and grid[i][j-1]<=limit:
                if dfs(i,j-1,limit):
                    return True
            return False

        N=len(grid)
        if grid[0][0]>N*N-1-N or grid[N-1][N-1]>N*N-1-N:
            return max(grid[0][0],grid[N-1][N-1])
        l=max(grid[0][0],grid[N-1][N-1])
        r=N*N-N
        while l<=r:
            mid=(l+r)//2
            visited=[[False for i in range(N)] for j in range(N)]
            if dfs(0,0,mid):
                r=mid-1
            else:
                l=mid+1
        return l
            
grid=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
c=Solution().swimInWater(grid)       

        

