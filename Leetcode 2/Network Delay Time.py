from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        def dfs(u):
            List.remove(u)
            if List:
                mindistance=10000
                for item in d[u]:
                    distance[item[0]-1]=min(distance[item[0]-1],distance[u-1]+item[1])
                # get min distance
                v=-1
                for vertice in List:
                    if distance[vertice-1]<mindistance:
                        v=vertice
                        mindistance=distance[vertice-1]
                if v!=-1:
                    dfs(v)
        distance=[10000 for i in range(N)]
        distance[K-1]=0
        d=defaultdict(list)
        for x,y,z in times:
            d[x].append([y,z])
        List=set([i for i in range(1,N+1)])
        dfs(K)
        length=max(distance)
        return length if length!=10000 else -1

times=[[1,2,1]]
N=2
K=2
c=Solution().networkDelayTime(times,N,K)

