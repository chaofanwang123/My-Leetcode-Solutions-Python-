class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        count=-1
        grid2=[[n**2 for i in range(n)] for j in range(n)]
        grid2[0][0]=grid[0][0]
        while count!=0:
            count=0
            for i in range(n):
                for j in range(n):
                    neighbor=[]
                    if i+1<n and grid:
                        neighbor.append(grid[i+1][j])
                    if i-1>=0:
                        neighbor.append(grid[i-1][j])
                    if j+1<n:
                        neighbor.append(grid[i][j+1])
                    if j-1>=0:
                        neighbor.append(grid[i][j-1])
                    minvalue=min(neighbor)
                    if minvalue>grid[i][j]:
                        count+=1
                        grid[i][j]=minvalue
        return grid[n-1][n-1]
        
grid=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
c=Solution().swimInWater(grid)               
        

