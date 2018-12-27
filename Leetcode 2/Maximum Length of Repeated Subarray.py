class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m=len(A)
        n=len(B)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        maxl=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    maxl=max(maxl,dp[i][j])
        return maxl
class Solution2:
    def findLength2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0
        A,res,sub = '#' + '#'.join(map(str,A)) + '#',0,'#'
        #print (A)
        for ch in B:
            sub += str(ch) + '#'
            if sub in A:
                res += 1
            else:
                sub = sub[sub[1:].index('#') + 1:]
        return res
A=[1,2,3,2,1,3,2,1,4]
B=[3,2,1,4,7]
c=Solution2().findLength2(A,B)