class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        dp=[[1]]
        for i in range(1,numRows):
            temp=[dp[-1][j-1]+dp[-1][j] for j in range(1,i)]
            dp.append([1]+temp+[1])
        return dp


