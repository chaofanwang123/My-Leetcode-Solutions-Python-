class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(x,y):
            while y:
                x,y=y,x%y
            return x
        if q==0:
            return 0
        if q==p:
            return 1
        factor=gcd(p,q)
        m,n=q//factor,p//factor
        if m%2:
            return 1 if n%2 else 2
        else:
            return 0
        
p=50
q=30
c=Solution().mirrorReflection(p,q)            
        

