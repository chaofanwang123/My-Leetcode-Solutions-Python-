from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs1(u,vertice):
            # return the # of subtree nodes and total distance of nodes to u in the subtrees rooted at u
            n=len(d[u])-1
            count=n
            distance=n
            for v in d[u]:
                if v!=vertice:
                    x,y=dfs1(v,u)
                    count+=x
                    distance+=y+x
            nodes_count[u]+=count
            totaldistance[u]+=distance          
            return [count,distance]
        def dfs2(u,vertice):
            for v in d[u]:
                if v!=vertice:
                    totaldistance[v]=totaldistance[u]-(nodes_count[v]+1)+N-nodes_count[v]-1
                    dfs2(v,u)
        if edges==[]:
            return [0]
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        nodes_count=[0 for i in range(N)]
        totaldistance=[0 for i in range(N)]
        nodes_count[edges[0][0]]=1
        totaldistance[edges[0][0]]=1
        dfs1(edges[0][0],edges[0][0])
        dfs2(edges[0][0],edges[0][0])
        return totaldistance
        
N = 6
edges = []
c=Solution().sumOfDistancesInTree(N,edges)