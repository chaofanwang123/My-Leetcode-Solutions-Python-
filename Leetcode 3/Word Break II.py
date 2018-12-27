class Solution:
    def check(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
        
    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0: Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])
    
    def wordBreak(self, s, wordDict):
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

