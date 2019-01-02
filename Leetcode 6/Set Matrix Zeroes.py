class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        v=set([])
        for i in range(m):
            count=0
            for j in range(n):
                if matrix[i][j]==0:
                    count+=1
                    v.add(j)
            if count!=0:
                matrix[i]=[0]*n
                matrix[i][0]='#'
        for i in range(m):
            if matrix[i][0]=='#':
                matrix[i][0]=0
            else:
                for j in v:
                    matrix[i][j]=0

matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
c=Solution().setZeroes(matrix)

