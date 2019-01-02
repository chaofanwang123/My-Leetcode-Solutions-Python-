class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find_parent(parent,i):
            if parent[i] == -1:
                return i
            if parent[i]!= -1:
                return find_parent(parent,parent[i])
        N=len(edges)
        parent=[-1]*(N+1)
        for i in range(N):
            v1,v2=edges[i][0],edges[i][1]
            x=find_parent(parent,v1)
            y=find_parent(parent,v2)
            if x==y:
                return edges[i]
            parent[x]=y
                    
edges=[[2,1],[3,1],[4,2],[1,4]]
c=Solution().findRedundantConnection(edges)
