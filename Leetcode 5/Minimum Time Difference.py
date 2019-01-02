class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n=len(timePoints)
        List=[[]]*n
        for i in range(n):
            s1,s2=timePoints[i].split(':')
            List[i]=int(s1)*60+int(s2)
        List.sort()
        minv=1440-(List[-1]-List[0])
        for i in range(1,n):
            minv=min(minv,List[i]-List[i-1],1440-(List[i]-List[i-1]))
        return minv

timePoints=["05:31","22:08","00:35"]
c=Solution().findMinDifference(timePoints)