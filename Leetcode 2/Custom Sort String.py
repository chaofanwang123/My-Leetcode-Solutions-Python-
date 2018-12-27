class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S or not T:
            return T
        vset=set(T)
        s=list(S)
        i=len(s)-1
        while i>=0:
            if s[i] in vset:
                vset.remove(s[i])
                s[i]=s[i]*T.count(s[i])   
            else:
                s[i]=''
            i-=1
        s1=''.join(s)
        for letter in vset:
            s1+=letter*T.count(letter)
        return s1
            
S="kqep"
T="pekeq" 
c=Solution().customSortString(S, T)
        
        

