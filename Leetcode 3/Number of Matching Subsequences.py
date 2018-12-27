from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d=defaultdict(list)
        for i in range(len(S)):
            d[S[i]].append(i)
        string='abcdefghijklmnopqrstuvwxyz'
        count=0
        for word in words:
            d2={letter:0 for letter in string}
            if word[0] in d:
                index=d[word[0]][0]
                d2[word[0]]+=1
                note=0
                for i in range(1,len(word)):
                    if word[i] in d:
                        m=len(d[word[i]])
                        j=d2[word[i]]
                        while j<m and d[word[i]][j]<index:
                            j+=1
                        if j==m:
                            note=1
                            break
                        index=d[word[i]][j]
                        d2[word[i]]=j+1
                    else:
                        note=1
                        break
                if note==0:
                    count+=1
        return count
            
S = "abcde"
words = ["a", "bb", "acd", "ace"]
c=Solution().numMatchingSubseq(S,words)
