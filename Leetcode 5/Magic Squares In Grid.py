class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        if m<3 or n<3:
            return 0
        count=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==5:
                    if grid[i][j-1]==1 and grid[i][j+1]==9:
                        if grid[i-1][j-1:j+2]==[6,7,2] and grid[i+1][j-1:j+2]==[8,3,4]:
                            count+=1
                        elif grid[i-1][j-1:j+2]==[8,3,4] and grid[i+1][j-1:j+2]==[6,7,2]:
                            count+=1
                    elif grid[i][j-1]==9 and grid[i][j+1]==1:
                        if grid[i-1][j-1:j+2]==[2,7,6] and grid[i+1][j-1:j+2]==[4,3,8]:
                            count+=1
                        elif grid[i-1][j-1:j+2]==[4,3,8] and grid[i+1][j-1:j+2]==[2,7,6]:
                            count+=1
                    elif grid[i][j-1]==3 and grid[i][j+1]==7:
                        if grid[i-1][j-1:j+2]==[8,1,6] and grid[i+1][j-1:j+2]==[4,9,2]:
                            count+=1
                        elif grid[i-1][j-1:j+2]==[4,9,2] and grid[i+1][j-1:j+2]==[8,1,6]:
                            count+=1
                    elif grid[i][j-1]==7 and grid[i][j+1]==3:
                        if grid[i-1][j-1:j+2]==[6,1,8] and grid[i+1][j-1:j+2]==[2,9,4]:
                            count+=1
                        elif grid[i-1][j-1:j+2]==[2,9,4] and grid[i+1][j-1:j+2]==[6,1,8]:
                            count+=1
        return count
grid=[[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]                       
c=Solution().numMagicSquaresInside(grid)

