class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """    
        if n==0:
            return 1
        if n%2==0:
            return self.myPow(x,n//2)**2
        elif n>0:
            return self.myPow(x,(n-1)//2)**2*x
        else:
            return self.myPow(x,(n+1)//2)**2/x

c=Solution().myPow(2,10)