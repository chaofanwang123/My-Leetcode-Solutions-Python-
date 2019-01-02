from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        string=paragraph.lower()
        s=string.split()
        for i in range(len(s)):
            if s[i][-1] in ",!?';.":
                s[i]=s[i][:-1]
        d=Counter(s)
        maxl=0
        vset=set(banned)
        ans=None
        for word in d:
            if d[word]>maxl and word not in vset:
                ans=word
                maxl=d[word]
        return ans
paragraph = "a, a, a, a, b,b,b,c, c"
banned=["a"]
c=Solution().mostCommonWord(paragraph,banned)

