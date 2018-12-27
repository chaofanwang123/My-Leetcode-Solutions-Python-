class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(A)
        n=len(A[0])
        for i in range(m):
            A[i].reverse()
            for j in range(n):
                A[i][j]=1-A[i][j]
        return A
        

