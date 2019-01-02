class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        s.reverse()
        return ' '.join(s)

s="the sky is blue"
c=Solution().reverseWords(s)