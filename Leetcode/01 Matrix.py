class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(matrix)
        n=len(matrix[0])
        stack=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    stack.append([i,j])
                else:
                    matrix[i][j]='#'
        d=[[-1,0],[0,-1],[0,1],[1,0]]
        while stack!=[]:
            i,j=stack.pop(0)
            for a,b in d:
                x,y=i+a,j+b
                if 0<=x<m and 0<=y<n and matrix[x][y]=='#':
                    matrix[x][y]=matrix[i][j]+1
                    stack.append([x,y])
        return matrix

matrix=[[0,0,0],[0,1,0],[1,1,1]]
c=Solution().updateMatrix(matrix)