class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n=len(A)
        i=0
        while i<n-1:
            if A[i]<A[i+1]:
                i+=1
                while i<n-1 and A[i]<A[i+1]:
                    i+=1
                if i<n-1 and (A[i]!=i+1 or A[i+1]!=i):
                    return False
                i+=2
            else:
                if A[i]!=i+1 or A[i+1]!=i:
                    return False
                i+=2
        return True
class Solution2:
    def isIdealPermutation2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, v in enumerate(A):
            if abs(i-v) > 1:
                return False
        return True

A = [0,1,2,3,4,6,5]
c=Solution2().isIdealPermutation2(A)