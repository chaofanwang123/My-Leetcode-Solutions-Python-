class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[] or matrix==[[]]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        il,jl=left//n,left%n
        ir,jr=right//n,right%n
        if matrix[il][jl]==target or matrix[ir][jr]==target:
            return True
        if matrix[il][jl]>target or matrix[ir][jr]<target:
            return False
        while left<=right:
            mid=(left+right)//2
            i,j=mid//n,mid%n
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                right=mid-1
            else:
                left=mid+1
        return False

matrix = [
  [1],
  [10],
  [23]
]
c=Solution().searchMatrix(matrix,23)