gmailclass Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        vset=set(words)
        ans=[]
        if '' in vset:
            vset.remove('')
        minl,maxl=float('inf'),-float('inf')
        for word in words:
            minl=min(minl,len(word))
            maxl=max(maxl,len(word))
        for word in words:
            n=len(word)
            if n>=minl*2:
                dp=[False]*(n+1)
                dp[0]=True
                for i in range(minl,n):
                    for j in range(max(0,i-maxl),i-minl+1):
                        if dp[j] and word[j:i] in vset:
                            dp[i]=True
                            break
                for j in range(max(1,n-maxl),n-minl+1):
                    if dp[j] and word[j:n] in vset:
                        ans.append(word)
                        break                     
        return ans
        
words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
c=Solution().findAllConcatenatedWordsInADict(words)
