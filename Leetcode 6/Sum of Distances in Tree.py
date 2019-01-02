class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if N==1:
            return [0]
        d={}
        for u,v in edges:
            if u in d:
                d[u].append(v)
            else:
                d[u]=[v]
            if v in d:
                d[v].append(u)
            else:
                d[v]=[u]
        self.matrix=[[-1 for i in range(N)] for j in range(N)]
        List=[]
        for u in range(N):
            self.matrix[u][u]=0
            self.dfs(u,u,d,0)
            List.append(sum(self.matrix[u]))
        return List
    def dfs(self,vertice,u,d,depth):
        for v in d[u]:
            if self.matrix[vertice][v]==-1:
                self.matrix[vertice][v]=depth+1
                self.dfs(vertice,v,d,depth+1)
            
        

N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
c=Solution().sumOfDistancesInTree(N,edges)
