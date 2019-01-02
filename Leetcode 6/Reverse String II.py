class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s
        i=0
        while i<n:
            s1=s[i:i+k]
            s=s[:i]+s1[::-1]+s[i+k:]
            i+=2*k
        return s

