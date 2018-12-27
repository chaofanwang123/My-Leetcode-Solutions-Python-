from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S==T:
            return 0
        d=defaultdict(set)
        d2=defaultdict(set)
        for i in range(len(routes)):
            for j in routes[i]:
                d[j].add(i)
        for buses in d.values():
            for bus in buses:
                d2[bus]|=buses
        for item in d2:
            d2[item].remove(item)
        stack=list(d[S])
        pastset=set()
        count=1
        for i in d[S]:
            if i in d[T]:
                return 1
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                bus=stack.pop(0)
                for i in d2[bus]:
                    if i in d[T]:
                        return count
                    if i not in pastset:
                        pastset.add(i)
                        stack.append(i)
        return -1
            
routes = [[1, 2, 7], [3, 6, 7]]
S=1
T=6

c=Solution().numBusesToDestination(routes,S,T)                 

