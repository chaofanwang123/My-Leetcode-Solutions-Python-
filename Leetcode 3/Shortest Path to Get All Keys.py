class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        k=0
        d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        d2={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        start=(0,0)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    start=(i,j)
                if grid[i][j] in d:
                    k+=1
        final='1'*k
        stack=[(start[0],start[1],'0'*k)]
        count=0
        vset=set()
        steps=[(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            k=len(stack)
            count+=1
            while k>0:
                k-=1
                i,j,string=stack.pop(0)
                for nx,ny in steps:
                    x=nx+i
                    y=ny+j
                    if 0<=x<m and 0<=y<n and grid[x][y]!='#':
                        if grid[x][y] in d2:
                            if string[d2[grid[x][y]]]=='0':
                                continue
                        if grid[x][y] in d:
                            tempstring=string[:d[grid[x][y]]]+'1'+string[d[grid[x][y]]+1:]
                            if tempstring==final:
                                return count
                            temp=(x,y,tempstring)
                        else:
                            temp=(x,y,string)
                        if temp not in vset:
                            vset.add(temp)
                            stack.append(temp)
        return -1

grid=["@Aa"]
c=Solution().shortestPathAllKeys(grid)               

