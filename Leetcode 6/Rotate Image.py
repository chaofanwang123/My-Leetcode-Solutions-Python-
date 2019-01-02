class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(n):
            matrix[i].reverse()


matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
c=Solution().rotate(matrix)

