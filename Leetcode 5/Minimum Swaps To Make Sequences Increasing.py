class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n=len(A)
        dp1=[0]*n # min swaps when swapping A[i],B[i]
        dp1[0]=1
        dp2=[0]*n # min swaps when not swapping A[i], B[i]
        for i in range(1,n):
            if A[i]<=A[i-1] or B[i]<=B[i-1]:
                dp2[i]=dp1[i-1]
                dp1[i]=dp2[i-1]+1
            elif A[i]>B[i-1] and B[i]>A[i-1]:
                dp2[i]=min(dp2[i-1],dp1[i-1])
                dp1[i]=min(dp2[i-1],dp1[i-1])+1
            else:
                dp1[i]=dp1[i-1]+1
                dp2[i]=dp2[i-1]
        return min(dp1[-1],dp2[-1])
                
A=[0,3,5,8,9]
B=[2,1,4,6,9]        
c=Solution().minSwap(A,B)
