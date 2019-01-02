class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0])
        if n==0:
            return []
        if m==1:
            return matrix[0]
        if n==1:
            return [matrix[i][0] for i in range(m)]
        List=matrix.pop(0)
        for i in range(m-1):
            List.append(matrix[i].pop())
        temp=matrix.pop()
        temp.reverse()
        List+=temp
        for i in range(m-3,-1,-1):
            List.append(matrix[i].pop(0))
        return List+self.spiralOrder(matrix)
        
matrix=[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
c=Solution().spiralOrder(matrix)
