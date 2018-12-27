from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        n=len(pattern)
        d=defaultdict(list)
        for i in range(n):
            d[pattern[i]].append(i)
        vset=set()
        for item in d.values():
            vset.add(tuple(item))
        ans=[]
        for word in words:
            d=defaultdict(list)
            note=0
            for i in range(n):
                d[pattern[i]].append(i)
            for item in d.values():
                if tuple(item) not in vset:
                    note=1
                    break
            if note==0:
                ans.append(word)
        return ans

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"        
c=Solution().findAndReplacePattern(words, pattern)
        

