from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = defaultdict(set)
        for u, v in edges:
            children[u].add(v)
            children[v].add(u)
        leaves = [x for x in range(n) if len(children[x]) <= 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                    if len(children[y]) == 1:
                        newLeaves.append(y)
            leaves = newLeaves
        return leaves
    

class Solution2:
    def findMinHeightTrees2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]                                    
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
            
        length=n
        List=[]
        for i in range(n):
            depth=0
            stack=[i]
            visited=[False]*n
            while stack and depth<=length:
                depth+=1
                temp=[]
                for u in stack:
                    visited[u]=True
                    for v in d[u]:
                        if not visited[v]:
                            temp.append(v)
                stack=temp
            if not stack:
                if depth<length:
                    List=[i]
                    length=depth
                elif depth==length:
                    List.append(i)
        return List

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
c=Solution().findMinHeightTrees(n,edges)               

