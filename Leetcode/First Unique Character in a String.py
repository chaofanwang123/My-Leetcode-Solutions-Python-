from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=Counter(s)
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1

