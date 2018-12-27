class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s=list(S)
        for i,word,newword in zip(indexes,sources,targets):
            n=len(word)
            if S[i:i+n]==word:
                s[i]=newword
                for j in range(i+1,i+n):
                    s[j]=''
        return ''.join(s)
            
S="abcd"
indexes=[0, 2]
sources=["a", "cd"]
targets=["eee", "ffff"]
c=Solution().findReplaceString(S, indexes, sources, targets)