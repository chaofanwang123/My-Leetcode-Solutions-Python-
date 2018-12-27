class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """                 
        n=len(graph)
        d=[[] for i in range(n)]
        for i in range(n):
            for j in graph[i]:
                d[j].append(i)
        stack=[]
        for i in range(n):
            if graph[i]==[]:
                stack.append(i)
        List=[]
        while stack!=[]:
            vertice=stack.pop(0)
            List.append(vertice)
            for item in d[vertice]:
                graph[item].remove(vertice)
                if graph[item]==[]:
                    stack.append(item)
        return List
    
class Solution2:
    def eventualSafeNodes2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u):
            if graph[u]==[]:
                visited[u]=True
                return
            stack[u]=True
            for v in graph[u]:
                if stack[v]:
                    stack2=[]
                    for i in range(n):
                        if stack[i]==True and visited[i]==-1:
                            stack2.append(i)
                    while stack2!=[]:
                        vertice=stack2.pop(0)
                        visited[vertice]=False
                        for item in d[vertice]:
                            if visited[item]==-1:
                                visited[item]=False
                                stack2.append(item)
            for v in graph[u]:
                if visited[v]==-1:
                    dfs(v)
            stack[u]=False                    
                    
        n=len(graph)
        visited=[-1 for i in range(n)]
        stack=[False for i in range(n)]
        d=[[] for i in range(n)]
        for i in range(n):
            for j in graph[i]:
                d[j].append(i)
        for i in range(n):
            if visited[i]==-1:
                dfs(i)
        List=[]
        for i in range(n):
            if visited[i]:
                List.append(i)
        return List

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
c=Solution().eventualSafeNodes(graph)