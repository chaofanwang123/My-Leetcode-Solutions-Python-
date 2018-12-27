import bisect
class RangeModule:

    def __init__(self):
        self.List=[]
        
    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if not self.List or left>self.List[-1]:
            self.List+=[left,right]
            return
        if right<self.List[0]:
            self.List=[left,right]+self.List
            return
        i=bisect.bisect_left(self.List,left)
        j=bisect.bisect_right(self.List,right)
        if i%2:
            if j%2:
                self.List[i:j]=[]
            else:
                self.List[i:j]=[right]
        else:
            if j%2:
                self.List[i:j]=[left]
            else:
                self.List[i:j]=[left,right]
                

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i=bisect.bisect_right(self.List,left)
        j=bisect.bisect_left(self.List,right)
        if i%2 and i==j:
            return True
        return False
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if not self.List or left>self.List[-1] or right<self.List[0]:
            return
        i=bisect.bisect_left(self.List,left)
        j=bisect.bisect_right(self.List,right)
        if i%2:
            if j%2:
                self.List[i:j]=[left,right]
            else:
                self.List[i:j]=[left]
        else:
            if j%2:
                self.List[i:j]=[right]
            else:
                self.List[i:j]=[]
        
obj=RangeModule()
obj.addRange(10,20)
obj.removeRange(14,16)
obj.queryRange(10,14)
obj.queryRange(13,15)
obj.queryRange(16,17)
