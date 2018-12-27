class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<2:
            return 0
        i,j=0,2
        dif=A[1]-A[0]
        count=0
        while j<len(A):
            if A[j]-A[j-1]==dif:
                j+=1
            else:
                count+=(j-i-2)*(j-i-1)//2
                i=j-1
                dif=A[j]-A[j-1]
                j+=1
        count+=(j-i-2)*(j-i-1)//2
        return count

A = [1, 2, 3, 4]
c=Solution().numberOfArithmeticSlices(A)