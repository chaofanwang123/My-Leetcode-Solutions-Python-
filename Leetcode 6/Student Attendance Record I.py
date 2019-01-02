class Solution:
    def checkRecord(self, S):
        """
        :type s: str
        :rtype: bool
        """
        
        if S.count("A") > 1 or "LLL" in S:
            return False
        return True
                
s="AAAA"
c=Solution().checkRecord(s)
