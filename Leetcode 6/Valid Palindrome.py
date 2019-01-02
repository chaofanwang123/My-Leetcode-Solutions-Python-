import re
class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == ''.join(reversed(s))

s="0P"
c=Solution().isPalindrome(s)