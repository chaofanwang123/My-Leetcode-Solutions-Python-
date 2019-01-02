class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        start=0
        length=0
        count=0
        for i in range(len(A)):
            if L<=A[i]<=R:
                length=i-start+1
                count+=length
            elif A[i]<L and length!=0:
               count+=length
            elif A[i]>R:
                start=i+1
                length=0
        return count
               
A = [2, 1, 4, 3,4,3,5,1,4,3,1,1,2,3,4]
L = 2
R = 4
c=Solution().numSubarrayBoundedMax(A,L,R)
