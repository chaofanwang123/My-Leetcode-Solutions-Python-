class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        d=set(A)
        maxc=0
        for i in range(n-1):
            for j in range(i+1,n):
                temp1,temp2=A[i],A[j]
                temp3=temp1+temp2
                count=2
                while temp3<=A[-1] and temp3 in d:
                    count+=1
                    temp1,temp2=temp2,temp3
                    temp3=temp1+temp2
                if count>2:
                    maxc=max(maxc,count)
        return maxc

A=[1,2,3,4,5,6,7,8]
c=Solution().lenLongestFibSubseq(A)
