class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            S=S.lower()
            index=S.index('@')
            return S[0]+'*'*5+S[index-1]+S[index:]
        else:
            s=''
            for letter in S:
                if letter in '0123456789':
                    s+=letter
            n=len(s)
            if n>10:
                return '+'+'*'*(n-10)+'-'+'*'*3+'-'+'*'*3+'-'+s[n-4:]
            else:
                return '*'*3+'-'+'*'*3+'-'+s[n-4:]

S="86-(10)12345678"
c=Solution().maskPII(S)
