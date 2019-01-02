class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(graph, node, parent, count, result):
            for nei in graph[node]:
                if nei != parent:
                    dfs(graph, nei, node, count, result)
                    count[node] += count[nei]
                    result[node] += result[nei]+count[nei]

        def dfs2(graph, node, parent, count, result,N):
            for nei in graph[node]:
                if nei != parent:
                    result[nei] = result[node]-count[nei] + N-count[nei]
                    dfs2(graph, nei, node, count, result,N)

        d={}
        for u, v in edges:
            if u in d:
                d[u].append(v)
            else:
                d[u]=[v]
            if v in d:
                d[v].append(u)
            else:
                d[v]=[u]

        count = [1] * N
        result = [0] * N

        dfs(d, 0, None, count, result)
        dfs2(d, 0, None, count, result,N)
        return result

N=6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

c=Solution().sumOfDistancesInTree(N,edges)