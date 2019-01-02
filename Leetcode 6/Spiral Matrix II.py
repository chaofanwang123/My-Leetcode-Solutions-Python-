class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        matrix=[[0 for i in range(n)] for j in range(n)]
        matrix[0]=[i for i in range(1,n+1)]
        for i in range(1,n-1):
            matrix[i][-1]=n+i
            matrix[i][0]=4*n-3-i
        for j in range(n):
            matrix[-1][j]=3*n-2-j
        i=1
        j=1
        direction='right'
        value=4*n-3
        while matrix[i][j]==0:
            matrix[i][j]=value
            value+=1
            if direction=='right':
                j+=1
                if matrix[i][j]!=0:
                    j-=1
                    i+=1
                    direction='down'
                continue
            if direction=='down':
                i+=1
                if matrix[i][j]!=0:
                    i-=1
                    j-=1
                    direction='left'
                continue
            if direction=='left':
                j-=1
                if matrix[i][j]!=0:
                    j+=1
                    i-=1
                    direction='up'
                continue
            if direction=='up':
                i-=1
                if matrix[i][j]!=0:
                    i+=1
                    j+=1
                    direction='right'
                continue
        return matrix
c=Solution().generateMatrix(1)

