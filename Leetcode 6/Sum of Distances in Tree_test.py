class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(root,backroot,d):
            b=d[root].index(backroot)
            del d[root][b]
            if d[root]!=[]:
                n=len(d[root])
                nodes=[[]]*n
                for i in range(n):
                    nodes[i]=dfs(d[root][i],root,d)
                    for item in nodes[i]:
                        nodes[i][item]+=1
                        self.List[item]+=nodes[i][item]
                        self.List[root]+=nodes[i][item]
                    
                for i in range(n):
                    for j in range(i+1,n):
                        for u in nodes[i]:
                            for v in nodes[j]:
                                self.List[u]+=(nodes[i][u]+nodes[j][v])
                                self.List[v]+=(nodes[i][u]+nodes[j][v])
                #combine
                for i in range(1,n):
                    nodes[0].update(nodes[i])
                nodes[0].update({root:0})
                return nodes[0]
            else:
                return {root:0}
            
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
        self.List=[0]*N
        d[edges[0][0]].insert(0,'#')
        dfs(edges[0][0],'#',d)
        return self.List

        

N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
#edges=[[2,0],[1,0]]
c=Solution().sumOfDistancesInTree(N,edges)


