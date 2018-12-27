class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def helper(s):
            n=len(s)
            if n==1:
                return [s]
            List=[]
            if s[0]!='0':
                List=[s]
            for i in range(1,n):
                s1,s2=s[:i],s[i:]
                if s2[-1]!='0' and (len(s1)<2 or s1[0]!='0'):
                    List.append(s1+'.'+s2)
            return List
                    
        s=S[1:-1]
        ans=[]
        for i in range(1,len(s)):
            s1,s2=s[:i],s[i:]
            List1,List2=helper(s1),helper(s2)
            if List1 and List2:
                ans+=['('+string1+', '+string2+')' for string1 in List1 for string2 in List2]
        return ans
        
S="(100)"
c=Solution().ambiguousCoordinates(S)