class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        List=s.split()
        return ' '.join(word[::-1] for word in List)

