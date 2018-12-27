class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if n<=1:
            return 0
        B=[0]*n
        C=[0]*n
        B[0]=A[0]
        C[n-1]=A[n-1]
        for i in range(1,n):
            B[i]=B[i-1]+A[i]
            C[n-1-i]=C[n-i]+A[n-1-i]
        ans=sum(A[i]*i for i in range(n))
        temp=ans
        for i in range(n-1,0,-1):
            temp=temp+B[i-1]+C[i]-A[i]*n
            ans=max(ans,temp)
        return ans

A = [4, 3, 2, 6]
c=Solution().maxRotateFunction(A)
            

