class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        word='abcdefghijklmnopqrstuvwxyz'
        d={}
        for i in range(26):
            d[word[i]]=i
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        s=list(S)
        for i in range(len(shifts)):
            s[i]=word[(d[s[i]]+shifts[i])%26]
        return ''.join(s)

