class Solution:
    def minCut(self, s):
        n=len(s)
        dp = [0 for i in range(n+1)]
        p = [[False for i in range(n)] for j in range(n)]
        for i in range(n+1):
            dp[i] = n - i
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1

class Solution3:
    def minCut3(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [i for i in range(n)]
        isPal = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    if j==0:
                        dp[i]=1
                        break
                    dp[i]=min(dp[i],dp[j-1]+1)
        return dp[-1]


class Solution2:
    def minCut2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i - r1 >= 0 and i + r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            while i - r2 -1 >= 0 and i + r2 < len(s) and s[i -r2-1] == s[i + r2]:
                cut[i + r2 + 1] = min(cut[i + r2 + 1], cut[i -r2-1] + 1)
                r2 += 1
        return cut[-1]

s="aabbaacasaaasd"
c=Solution().minCut(s)