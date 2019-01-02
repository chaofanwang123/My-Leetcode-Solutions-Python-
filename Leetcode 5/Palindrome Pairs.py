class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n=len(words)
        if n<2:
            return []
        ans=[]
        d={}
        for i in range(n):
            d[words[i]]=i
        wordset=set(words)
        if '' in wordset:
            index=d['']
            del words[index]
            for word in words:
                if word==word[::-1]:
                    ans+=[[index,d[word]],[d[word],index]]
        for word in words:
            L=len(word)
            s=word[::-1]
            if s!=word and s in wordset:
                ans.append([d[word],d[s]])
            for i in range(1,L):
                s1,s2=word[:i],word[L-1:i-1:-1]
                s3,s4=word[i:],word[i-1::-1]
                if s1==s1[::-1] and s2 in wordset:
                    ans.append([d[s2],d[word]])
                if s3==s3[::-1] and s4 in wordset:
                    ans.append([d[word],d[s4]])
        return ans

words=["a",""]
c=Solution().palindromePairs(words)
