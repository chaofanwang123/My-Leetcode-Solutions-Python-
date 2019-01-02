class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i,j,matrix,m,n):
            if matrix2[i][j]!=[]:
                return matrix2[i][j]
            else:
                a=0
                b=0
                c=0
                d=0
                if i+1<m and matrix[i+1][j]>matrix[i][j]:
                    a=dfs(i+1,j,matrix,m,n)
                if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                    b=dfs(i-1,j,matrix,m,n)
                if j+1<n and matrix[i][j+1]>matrix[i][j]:
                    c=dfs(i,j+1,matrix,m,n)
                if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                    d=dfs(i,j-1,matrix,m,n)
                matrix2[i][j]=1+max(a,b,c,d)
                return matrix2[i][j]          
        if matrix==[]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        matrix2=[[[] for i in range(n)] for j in range(m)]
        maxv=0
        for i in range(m):
            for j in range(n):
                maxv=max(maxv,dfs(i,j,matrix,m,n))
        return maxv

matrix=[[3,4,5],[3,2,6],[2,2,1]]
c=Solution().longestIncreasingPath(matrix)

