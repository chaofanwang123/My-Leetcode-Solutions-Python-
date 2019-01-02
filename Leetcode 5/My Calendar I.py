class MyCalendar:

    def __init__(self):
        self.List=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.List:
            self.List.append([start,end])
            return True
        if end<=self.List[0][0]:
            self.List.insert(0,[start,end])
            return True
        i=0
        n=len(self.List)
        while i<n and end>self.List[i][0]:
            i+=1
        if end<=self.List[i-1][1]:
            return False
        if start>=self.List[i-1][1]:
            self.List.insert(i,[start,end])
            return True
        return False
        
obj=MyCalendar()
obj.book(10,20)
obj.book(15,25)
obj.book(20,30)       
            

