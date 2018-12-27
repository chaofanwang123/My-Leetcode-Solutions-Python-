from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []
        m,L=len(words[0]),len(words[0])*len(words)
        d=Counter(words)
        ans=[]
        for i in range(len(s)-L+1):
            string=s[i:i+L]
            List=[string[j:j+m] for j in range(0,L,m)]
            if Counter(List)==d:
                ans.append(i)
        return ans
s = "wordgoodgoodgoodbestword"
words=["word","good","best","good"]
c=Solution().findSubstring(s,words)