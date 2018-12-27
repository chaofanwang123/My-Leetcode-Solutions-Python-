class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if n<=2:
            return 0
        dp=[{} for i in range(n)]
        dp[1][A[1]-A[0]]=1
        count=0
        for i in range(2,n):
            for j in range(i):
                dif=A[i]-A[j]
                if dif not in dp[i]:
                    dp[i][dif]=1
                else:
                    dp[i][dif]+=1
                if dif in dp[j]:
                    dp[i][dif]+=dp[j][dif]
                    count+=dp[j][dif]
        return count

A=[2,2,3,4]
c=Solution().numberOfArithmeticSlices(A)
                        
                    
