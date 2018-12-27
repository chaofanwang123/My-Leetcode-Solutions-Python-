class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n=len(s),len(t)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

class Solution2:
    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        acc = [0] * len(t) + [1]
        index = dict()
        for i, c in enumerate(t):
            if c not in index:
                index[c] = []
            index[c].append(i)
        for c in s[::-1]:
            if c in index:
                for j in index[c]:
                    acc[j] += acc[j + 1]
        return acc[0]
    
S ="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
T="bddabdcae"
c=Solution().numDistinct(S,T)