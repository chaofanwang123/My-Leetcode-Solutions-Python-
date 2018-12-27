class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod=pow(10,9)+7
        A.sort()
        dp=0
        n=len(A)
        pow2=[1]*n
        for i in range(1,n):
            pow2[i]=2*pow2[i-1]
        for i in range(n):
            dp+=A[i]*pow2[i]
            dp-=A[i]*pow2[n-1-i]
            dp%=mod
        return dp

A=[2,1,3]
c=Solution().sumSubseqWidths(A)