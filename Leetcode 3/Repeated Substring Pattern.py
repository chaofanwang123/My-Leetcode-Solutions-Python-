class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n<2:
            return False
        for i in range(2,n+1):
            if n%i==0:
                length=n//i
                s1=s[:length]
                if s[length:]==s1*(i-1):
                    return True
        return False

