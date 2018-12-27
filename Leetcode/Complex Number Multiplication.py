class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x,y=[0,0],[0,0]
        a1=a.split('+')
        x[0],x[1]=int(a1[0]),int(a1[1][:-1])
        b1=b.split('+')
        y[0],y[1]=int(b1[0]),int(b1[1][:-1])
        if '+' in a and '+' in b:
            return str(x[0]*y[0]-x[1]*y[1])+'+'+str(x[0]*y[1]+x[1]*y[0])+'i'
        elif '+' in a and '-' in b:
            return str(x[0]*y[0]+x[1]*y[1])+'+'+str(-x[0]*y[1]+x[1]*y[0])+'i'
        elif '-' in a and '+' in b:
            return str(x[0]*y[0]+x[1]*y[1])+'+'+str(x[0]*y[1]-x[1]*y[0])+'i'
        else:
            return str(x[0]*y[0]-x[1]*y[1])+'+'+str(-x[0]*y[1]-x[1]*y[0])+'i'

a="1+1i"
b="1+1i"
c=Solution().complexNumberMultiply(a,b)