class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            if timeSeries[i] < timeSeries[i - 1] + duration:
                total -= timeSeries[i - 1] + duration - timeSeries[i]
        return total
class Solution2:
    def findPoisonedDuration2(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        st = ed = 0
        ans = 0
        for t in timeSeries:
            if t >= ed:
                ans += ed - st
                st = t
                ed = st + duration
            else:
                ed = t + duration
        ans += ed - st
        return ans                    
            
timeSeries=[1,2]
duration=2
c=Solution().findPoisonedDuration2(timeSeries,duration)