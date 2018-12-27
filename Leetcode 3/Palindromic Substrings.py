class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n<=1:
            return n
        dp=1
        for i in range(1,n):
            count=1
            for j in range(i):
                string=s[j:i+1]
                if string==string[::-1]:
                    count+=1
            dp+=count
        return dp

class Solution2(object):
    def countSubstrings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count