class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        m,n=len(A),len(B)
        if m<2 or m!=n:
            return False
        List=[]
        count=0
        for i in range(n):
            if A[i]!=B[i]:
                count+=1
                List.append(i)
        if count==0 and len(set(A))<n:
            return True
        if count==2 and A[List[1]]==B[List[0]] and A[List[0]]==B[List[1]]:
            return True
        return False

A = "aaaaaaabc"
B = "aaaaaaacb"
c=Solution().buddyStrings(A,B)
