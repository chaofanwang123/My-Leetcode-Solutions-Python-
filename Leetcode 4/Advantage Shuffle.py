class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """    
        n=len(A)
        A.sort(reverse=True)
        B1=[(B[i],i) for i in range(n)]
        B1.sort(reverse=True)
        if A[0]<=B1[-1][0] or A[-1]>B1[0][0]:
            return A
        C=[0]*n
        i,j=0,0
        List=[]
        while i<n and j<n:
            if A[i]<=B1[j][0]:
                List.append(B1[j][1])
                j+=1
            else:
                C[B1[j][1]]=A[i]
                i+=1
                j+=1
        for j,index in enumerate(List):
            C[index]=A[i+j]
        return C

class Solution2:
    def advantageCount2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        idxs = sorted(range(len(B)), key=lambda idx: B[idx])
        
        lo = 0
        hi = len(idxs) - 1
        
        for a in sorted(A):
            if a > B[idxs[lo]]:
                A[idxs[lo]] = a
                lo += 1
            else:
                A[idxs[hi]] = a
                hi -= 1
                
        return A
A = [14]
B = [13]      
c=Solution().advantageCount(A,B)                
        
