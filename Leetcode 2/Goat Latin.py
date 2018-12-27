class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s=S.split()
        for i in range(len(s)):
            if s[i][0] in 'aeiouAEIOU':
                s[i]+='ma'
            else:
                s[i]=s[1:]+s[0]+'ma'
            s[i]+='a'*(i+1)
        return ' '.join(s)

