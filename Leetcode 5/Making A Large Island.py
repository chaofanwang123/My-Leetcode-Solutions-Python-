class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j,label):
            grid[i][j]=label
            a,b,c,d=0,0,0,0
            if i+1<n and grid[i+1][j]==1:
                a=dfs(i+1,j,label)
            if i-1>=0 and grid[i-1][j]==1:
                b=dfs(i-1,j,label)
            if j+1<n and grid[i][j+1]==1:
                c=dfs(i,j+1,label)
            if j-1>=0 and grid[i][j-1]==1:
                d=dfs(i,j-1,label)
            return 1+a+b+c+d
        n=len(grid)
        label=1
        arealist=[]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    label+=1
                    arealist.append(dfs(i,j,label))
        if arealist==[]:
            return 1
        maxarea=arealist[0]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    labelset=set()
                    if i+1<n and grid[i+1][j]!=0:
                        labelset.add(grid[i+1][j])
                    if i-1>=0 and grid[i-1][j]!=0:
                        labelset.add(grid[i-1][j])
                    if j+1<n and grid[i][j+1]!=0:
                        labelset.add(grid[i][j+1])
                    if j-1>=0 and grid[i][j-1]!=0:
                        labelset.add(grid[i][j-1])
                    m=len(labelset)
                    labelset=list(labelset)
                    labelset.sort()
                    if m==1:
                        maxarea=max(maxarea,arealist[labelset[0]-2]+1)
                    if m==2: 
                        maxarea=max(maxarea,arealist[labelset[-1]-2]+arealist[labelset[-2]-2]+1)
                    if m==3: 
                        maxarea=max(maxarea,arealist[labelset[-1]-2]+arealist[labelset[-2]-2]+arealist[labelset[-3]-2]+1)
                    if m==4: 
                        maxarea=max(maxarea,arealist[labelset[0]-2]+arealist[labelset[1]-2]+arealist[labelset[2]-2]+arealist[labelset[3]-2]+1)
        return maxarea

grid=[[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]
c=Solution().largestIsland(grid)