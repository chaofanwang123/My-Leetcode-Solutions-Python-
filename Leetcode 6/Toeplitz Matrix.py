class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m=len(matrix)
        if m==1:
            return True
        for i in range(1,m):
            if matrix[i-1][:-1]!=matrix[i][1:]:
                return False
        return True
