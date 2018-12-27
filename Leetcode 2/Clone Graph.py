# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(oldnode,d):
            if oldnode in d:
                return d[oldnode]
            newnode=UndirectedGraphNode(node.label)
            d[oldnode]=newnode
            for i in oldnode.neighbors:
                newnode.neighbors.append(dfs(i,d))
            return newnode
        return dfs(node,{})

node=UndirectedGraphNode(0)
node1=UndirectedGraphNode(1)
node2=UndirectedGraphNode(2)
node3=UndirectedGraphNode(2)
node.neighbors=[node1,node2]
node1.neighbors=[node2]
node2.neighbors=[node2]

c=Solution().cloneGraph(node)
                
