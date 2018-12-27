class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d={}
        for i,letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            d[i+1]=letter
        ans=''
        while n>=26:
            if n%26==0:
                ans='Z'+ans
                n=n//26-1
            else:
                ans=d[n%26]+ans
                n=n//26
        if n>0:
            ans=d[n]+ans
        return ans

c=Solution().convertToTitle(1000000001)