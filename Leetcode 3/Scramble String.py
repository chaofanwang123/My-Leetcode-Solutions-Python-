class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        n=len(s1)
        d1,d2={},{}
        for i in range(n):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1
        for item in d1:
            if item not in d2 or d1[item]!=d2[item]:
                return False
        for i in range(1,n):
            if self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i]):
                return True
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
        return False
s1 = "abcde"
s2 = "caebd"
c=Solution().isScramble(s1,s2)