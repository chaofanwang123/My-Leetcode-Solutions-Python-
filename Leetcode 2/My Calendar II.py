import bisect
class MyCalendarTwo(object):

    def __init__(self):
        self.one = []
        self.two = []
        
    def is_valid(self, start, end):
        if end <= start:
            return -1
        i = bisect.bisect_right(self.two, start)
        if i % 2:
            return -1
        j = bisect.bisect_left(self.two, end)
        if i != j:
            return -1
        return i
    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        t = self.is_valid(start, end)  
        if t == -1:
            return False
        i = bisect.bisect_right(self.one, start)
        j = bisect.bisect_left(self.one, end)
        
        if i % 2: 
            if j % 2:
                self.two[t:t] = [start] + self.one[i:j] + [end]
                self.one[i:j] = []
            else:
                self.two[t:t] = [start] + self.one[i:j]
                self.one[i:j] = [end]
        else:
            if j % 2:
                self.two[t:t] = self.one[i:j] + [end]
                self.one[i:j] = [start]
            else:
                self.two[t:t] = self.one[i:j]
                self.one[i:j] = [start, end]
        return True

