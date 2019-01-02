class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s and s[-1]==' ':
            s=s[:-1]
        i=len(s)-1
        while i>=0 and s[i]!=' ':
            i-=1
        return (len(s)-i-1)
s="Hello World"
c=Solution().lengthOfLastWord(s)
