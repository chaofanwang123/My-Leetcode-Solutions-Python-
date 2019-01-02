class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs1(x,y):
            pac.add((x,y))
            if x+1<m and (x+1,y) not in pac and matrix[x+1][y]>=matrix[x][y]:
                dfs1(x+1,y)
            if x-1>=0 and (x-1,y) not in pac and matrix[x-1][y]>=matrix[x][y]:
                dfs1(x-1,y)
            if y+1<n and (x,y+1) not in pac and matrix[x][y+1]>=matrix[x][y]:
                dfs1(x,y+1)
            if y-1>=0 and (x,y-1) not in pac and matrix[x][y-1]>=matrix[x][y]:
                dfs1(x,y-1)
        def dfs2(x,y):
            atl.add((x,y))
            if x+1<m and (x+1,y) not in atl and matrix[x+1][y]>=matrix[x][y]:
                dfs2(x+1,y)
            if x-1>=0 and (x-1,y) not in atl and matrix[x-1][y]>=matrix[x][y]:
                dfs2(x-1,y)
            if y+1<n and (x,y+1) not in atl and matrix[x][y+1]>=matrix[x][y]:
                dfs2(x,y+1)
            if y-1>=0 and (x,y-1) not in atl and matrix[x][y-1]>=matrix[x][y]:
                dfs2(x,y-1)
        if not matrix:
            return []
        pac,atl=set(),set()
        m=len(matrix)
        n=len(matrix[0])
        if m==1:
            return [[0,j] for j in range(n)]
        if n==1:
            return [[i,0] for i in range(m)]
        pac_list,atl_list=[],[]
        for j in range(n):
            pac_list.append((0,j))
            atl_list.append((m-1,j))
        for i in range(1,m):
            pac_list.append((i,0))
            atl_list.append((i-1,n-1))
        for i in pac_list:
            if i not in pac:
                dfs1(i[0],i[1])
        for i in atl_list:
            if i not in atl:
                dfs2(i[0],i[1])
        temp=pac&atl
        return [list(item) for item in temp]
        
matrix=[[3,3,3],[3,1,3],[0,2,4]]
c=Solution().pacificAtlantic(matrix)
