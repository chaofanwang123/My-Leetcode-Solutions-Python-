class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        vset=set()
        for word in A:
            n=len(word)
            s1=[word[i] for i in range(0,n,2)]
            s2=[word[i] for i in range(1,n,2)]
            s1.sort()
            s2.sort()
            vset.add(''.join(s1)+''.join(s2))
        return len(vset)
        
A=["abcd","cdab","adcb","cbad"]
c=Solution().numSpecialEquivGroups(A)
