class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for i in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]!='*':
                break
            dp[0][j]=dp[0][j-1]
        DP=[False]*(n+1)
        DP[0]=True
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j]=DP[j-1]
                elif p[j-1]=='?' or p[j-1]==s[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                if dp[i][j]:
                    DP[j]=True
        return dp[-1][-1]

class Solution2:
    def isMatch2(self, s, p):
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False
    
s="aaaababbbabbbbaabbaaabbbbabbbbbabaaaabbbbbaaaabbbbbaaabbaaaabbabbabbabababaabbbbaabaaabbabbaabbababbbabbbbbaaabaaaababababbaaaabaabaaabbbbbbbbbabbbaabbaaaaaabbabaabaaabbbaaabaaabaaabaabbabaabbaaabaaabb"
p="bb*****b*ba*a**bb*b**aba**a*b*b*b*a*b*a*ba*b*a*a*****a*b***a*a**a**b**b***a*a***bbba*abb*abba*bab***"
c=Solution().isMatch(s,p)
                
            

