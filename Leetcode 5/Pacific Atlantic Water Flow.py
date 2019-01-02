class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i,j,matrix,m,n,visited,value,visited2):
            if visited2[i][j]:
                return True
            visited[i][j]=True
            if visited[0][0] and visited[m-1][n-1]:
                return True
            if i+1<m and visited[i+1][j]==False and matrix[i+1][j]<=value:
                if dfs(i+1,j,matrix,m,n,visited,value,visited2):
                    return True
            if i-1>=0 and visited[i-1][j]==False and matrix[i-1][j]<=value:
                if dfs(i-1,j,matrix,m,n,visited,value,visited2):
                    return True
            if j+1<m and visited[i][j+1]==False and matrix[i][j+1]<=value:
                if dfs(i,j+1,matrix,m,n,visited,value,visited2):
                    return True
            if j-1>=0 and visited[i][j-1]==False and matrix[i][j-1]<=value:
                if dfs(i,j-1,matrix,m,n,visited,value,visited2):
                    return True
            return False
        if matrix==[]:
            return []
        List=[]
        m=len(matrix)
        n=len(matrix[0])
        maxv=max(matrix[0][0],matrix[m-1][n-1])
        visited2=[[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]>=maxv:
                    visited=[[False for i in range(n)] for j in range(m)]
                    if dfs(i,j,matrix,m,n,visited,matrix[i][j],visited2):
                        List.append([i,j])
                        visited2[i][j]=True
        return List

matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
c=Solution().pacificAtlantic(matrix)

