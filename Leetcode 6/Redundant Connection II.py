class Solution(object):
    def findRedundantDirectedConnection(self, edges):
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
        descendant={}
        index=[]
        note=-1
        for i in range(N):
            v1,v2=edges[i][0],edges[i][1]
            if v2 in descendant:
                index=[descendant[v2],i]
                if note!=-1:
                    return edges[index[0]]
            else:
                descendant[v2]=i
                if note==-1:
                    x=find_parent(parent,v1)
                    y=find_parent(parent,v2)
                    if x==y:
                        note=i
                        if index!=[]:
                            return edges[index[0]]
                    parent[x]=y
        if index==[]:
            return edges[note]
        return edges[index[1]]

edges=[[3,4],[4,1],[1,2],[2,3],[5,1]]
#edges=[[2,1],[3,1],[4,2],[1,4]]
#edges=[[1,2], [2,3], [3,4], [4,1], [1,5]]
c=Solution().findRedundantDirectedConnection(edges)