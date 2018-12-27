class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        dp=10
        factor=9
        for i in range(2,min(n+1,10)):
            temp=9*factor
            dp+=temp
            factor=factor*(10-i)
        return dp
            
