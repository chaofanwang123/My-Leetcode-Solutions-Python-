class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n=len(A)
        d1=[]
        d2=[]
        for i in range(n):
            for j in range(n):
                if A[i][j]==1:
                    d1.append([i,j])
                if B[i][j]==1:
                    d2.append([i,j])
        d3={}
        for u1,v1 in d1:
            for u2,v2 in d2:
                x=u2-u1
                y=v2-v1
                if (x,y) not in d3:
                    d3[(x,y)]=1
                else:
                    d3[(x,y)]+=1
        return max(d3.values()) if d3 else 0

A = [[0]]
B = [[0]]
c=Solution().largestOverlap(A,B)