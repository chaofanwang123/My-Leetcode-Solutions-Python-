class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        l, count, i = [], 0, 0
        for j, v in enumerate(S):
            count = count+1 if v=='1' else count-1
            if count == 0:
                l.append('1' + self.makeLargestSpecial(S[i+1:j]) + '0')
                i = j + 1
        return ''.join(sorted(l)[::-1])

