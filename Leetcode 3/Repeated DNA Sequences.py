class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        vset=set()
        ans=set()
        for i in range(len(s)-9):
            if s[i:i+10] in vset:
                ans.add(s[i:i+10])
            else:
                vset.add(s[i:i+10])
        return list(ans)

