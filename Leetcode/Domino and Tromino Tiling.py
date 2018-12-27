class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<=2:
            return N
        dp0=[0]*N
        dp1=[0]*N
        dp0[0]=1
        dp0[1]=2
        dp1[1]=1
        for i in range(2,N):
            dp0[i]=dp0[i-1]+dp0[i-2]+2*dp1[i-1]
            dp1[i]=dp0[i-2]+dp1[i-1]
        return dp0[-1]%(pow(10,9)+7)
N=100
c=Solution().numTilings(N)

