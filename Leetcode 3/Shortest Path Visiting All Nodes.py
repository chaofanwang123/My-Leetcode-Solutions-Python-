class Solution:
    def shortestPathLength(self, graph):
        memo=set()
        final=1<<len(graph)-1
        q=[(i, 1<<i) for i in range(len(graph))]
        steps=0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1
        
graph=[[1,2,3],[0],[0],[0]]
c=Solution().shortestPathLength(graph)
