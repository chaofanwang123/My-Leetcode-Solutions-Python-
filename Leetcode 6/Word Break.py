class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        wordset=set(wordDict)
        minl=float('inf')
        maxl=0
        for word in wordset:
            minl=min(minl,len(word))
            maxl=max(maxl,len(word))
        minl=max(minl,1)
        if minl>n:
            return False
        for i in range(minl,n+1):
            for j in range(max(0,i-maxl),i-minl+1):
                if dp[j] and s[j:i] in wordset:
                    dp[i]=True
                    break
        return dp[-1]

