class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(u,group):
            for v in graph[u]:
                if v in d[group]:
                    return False
                d[1-group].add(v)
            visited[u]=True
            for v in graph[u]:
                if not visited[v]:
                    if not dfs(v,1-group):
                        return False
            return True
        A=set()
        B=set()
        A.add(0)
        d={0:A,1:B}
        n=len(graph)
        visited=[False for i in range(n)]
        for i in range(n):
            if not visited[i]:
                if not dfs(i,0):
                    return False
        return True
    
graph=[[1,3], [0,2], [1,3], [0,2]]
c=Solution().isBipartite(graph)

