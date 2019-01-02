class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1
        i=2
        s=A+A
        n=len(A)
        while B not in s:
            if s[n:] not in B:
                return -1
            i+=1
            s+=A
        return i
            
class Solution2:
    def repeatedStringMatch2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for i in range(1,len(A)//len(B)+3):
            if B in A*i:
                return i
        return -1
A="abcd"
B="cdabcdab"
c=Solution().repeatedStringMatch(A,B)
