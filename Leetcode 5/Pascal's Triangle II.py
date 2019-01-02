class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        dp=[1]
        for i in range(1,rowIndex+1):
            temp=[dp[j-1]+dp[j] for j in range(1,i)]
            dp=[1]+temp+[1]
        return dp


