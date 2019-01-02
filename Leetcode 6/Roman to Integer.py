class Solution:
    def romanToInt(self, s):
        d = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        ans=0
        s=s[::-1]
        last=None
        for x in s:
            if last and d[x]<last:
                ans-=2*d[x]
            ans+=d[x]
            last=d[x]
        return ans