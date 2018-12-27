class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if len(t)<len(s):
            return False
        for word in t:
            if word==s[0]:
                s=s[1:]
                if not s:
                    return True
        return False
                
s = "axc"
t = "ahbgdc"           
c=Solution().isSubsequence(s,t)
