class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(M)
        n=len(M[0])
        M2=[[0 for j in range(n)] for i in range(m)]
        step=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(m):
            for j in range(n):
                summ=M[i][j]
                count=1
                for u,v in step:
                    if 0<=i+u<m and 0<=j+v<n:
                        summ+=M[i+u][j+v]
                        count+=1
                M2[i][j]=summ//count
        return M2

