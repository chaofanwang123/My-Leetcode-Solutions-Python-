class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N=m-1+n-1
        P=min(m-1,n-1)
        s=1
        for i in range(P):
           s=s*(N-i)/(i+1)
        return int(s)

c=Solution().uniquePaths(7,3)

