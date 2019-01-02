# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import bisect
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        List=[]
        for interval in intervals:
            List+=[interval.start,interval.end]
        i=bisect.bisect_left(List,newInterval.start)
        j=bisect.bisect_right(List,newInterval.end)
        if i%2:
            if j%2:
                List[i:j]=[]
            else:
                List[i:j]=[newInterval.end]
        else:
            if j%2:
                List[i:j]=[newInterval.start]
            else:
                List[i:j]=[newInterval.start,newInterval.end]
        n=len(List)//2
        ans=[[]]*n
        for i in range(n):
            ans[i]=Interval(List[2*i],List[2*i+1])
        return ans

intervals=[[]]*5
intervals[0]=Interval(1,2)
intervals[1]=Interval(3,5)
intervals[2]=Interval(6,7)
intervals[3]=Interval(8,10)
intervals[4]=Interval(12,16)

newInterval=Interval(3,8)
c=Solution().insert(intervals,newInterval)

