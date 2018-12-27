class Solution:
    def dotproduct3(self,A,B):
        i=0
        j=0
        k=0
        sum=0
        m=len(A)
        n=len(B)
        C=[0]*(m+n)
        while i<m and j<n:
            if A[i]<B[j]:
                C[k]=A[i]
                i+=1
            elif A[i]>B[j]:
                C[k]=B[j]
                j+=1
            else:
                sum+=1
                i+=1
                j+=1
            k+=1
        if i==m:
            if C[k]==B[j]:
                sum+=1
        if j==n:
            if C[k]==A[i]:
                sum+=1
        return sum

A=[1,2,5,6]
B=[1,3,5,6,8]
c=Solution().dotproduct3(A,B)

