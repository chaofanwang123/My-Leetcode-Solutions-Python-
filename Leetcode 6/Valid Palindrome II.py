class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n<=2:
            return True
        while len(s)>=2 and s[-1]==s[0]:
            s=s[1:-1]
        if len(s)>2:
            s1,s2=s[:-1],s[1:]
            if s1!=s1[::-1] and s2!=s2[::-1]:
                return False
            return True
        return True

