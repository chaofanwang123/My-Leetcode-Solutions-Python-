class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total,n=sum(machines),len(machines)
        if total%n:
            return -1
        avg=total//n
        ans=times=0
        for m in machines:
            times += m - avg
            ans = max(ans, abs(times), m - avg)
        return ans
