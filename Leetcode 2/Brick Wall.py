from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d=defaultdict(int)
        width=sum(wall[0])
        for row in wall:
            x=0
            for j in row:
                x+=j
                d[x]+=1
        del d[width]
        return len(wall)-max(d.values()) if d else len(wall)
                

