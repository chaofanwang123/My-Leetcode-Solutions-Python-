class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        string='abcdefghijklmnopqrstuvwxyz'
        d={}
        for i in range(len(string)):
            d[string[i]]=i
        times=[0]*26
        i=1
        n=len(p)
        while i<=n:
            count=1
            times[d[p[i-1]]]=max(times[d[p[i-1]]],count)
            while i<n and (d[p[i-1]]+1)%26==d[p[i]]:
                i+=1
                count+=1
                times[d[p[i-1]]]=max(times[d[p[i-1]]],count)
            i+=1
        return sum(times)

p='cacasdajkdjaodjaojiadsojiadjsi'
c=Solution().findSubstringInWraproundString(p)