class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=triangle[0]
        for i in range(1,n):
            temp=[0]*(i+1)
            temp[0]=dp[0]+triangle[i][0]
            temp[-1]=dp[-1]+triangle[i][-1]
            for j in range(1,i):
                temp[j]=min(dp[j],dp[j-1])+triangle[i][j]
            dp=temp
        return min(dp)

triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
c=Solution().minimumTotal(triangle)