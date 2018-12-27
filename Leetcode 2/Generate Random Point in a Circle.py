import random
import math
class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r=radius
        self.xc,self.yc=x_center,y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        R=self.r*random.random()
        theta=2*math.pi*random.random()
        return [self.xc+R*math.cos(theta),self.yc+R*math.sin(theta)]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

