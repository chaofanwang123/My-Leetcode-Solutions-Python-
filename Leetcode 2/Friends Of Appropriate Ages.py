import bisect
class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        if ages[-1]<15:
            return 0
        if ages[0]<15:
            index=bisect.bisect_left(ages,15)
            ages=ages[index:]
        n=len(ages)
        count=0
        j=1
        for i in range(n-1):
            index=bisect.bisect_right(ages,ages[i],i+1)
            count+=index-i-1
            if j<n:
                j=bisect.bisect_left(ages,2*ages[i]-14,i+1)
            count+=j-i-1
        return count

ages=[16,17,18]#[54,23,102,90,40,74,112,74,76,21]
c=Solution().numFriendRequests(ages)