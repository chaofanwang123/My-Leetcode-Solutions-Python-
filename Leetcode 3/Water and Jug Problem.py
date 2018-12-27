class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z==x or z==y:
            return True
        if x==y:
            return z==0
        if x<y:
            x,y=y,x
        if z>(x+y):
            return False
        if y==0:
            return False
        if z%y==0:
            return True
        x1=x%y
        if x1==0:
            return False
        z1=z%y
        for i in range(1,y):
            if (i*x1)%y==z1:
                return True
        return False

x=0
y=2
z=1        
c=Solution().canMeasureWater(x,y,z)
