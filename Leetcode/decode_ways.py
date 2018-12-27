class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==1:
            if s=='0':
                return 0
            return 1
        if s[0]=='0':
            return 0
        dp0=1
        dp1=1
        for i in range(1,n):
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp2=dp0
                else:
                    return 0
            elif 10<int(s[i-1:i+1])<=26:
                dp2=dp0+dp1
            else:
                dp2=dp1
            dp0=dp1
            dp1=dp2
        return dp2
    
s="36"
c=Solution().numDecodings(s)

