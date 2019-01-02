class Solution2(object):
    def shortestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s
        for i in range(n,0,-1):
            s1,s2=s[:i],s[i:]
            if s1==s1[::-1]:
                return s2[::-1]+s1+s2

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        l = s + "#" +  rev_s
        p = [0] * len(l)
        for i in range(1,len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[:len(s) - p[-1]] + s
            
s='abadc'
c=Solution().shortestPalindrome(s)            
            
            
        

