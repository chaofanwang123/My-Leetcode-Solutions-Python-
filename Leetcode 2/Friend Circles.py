class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i,M,visited,n):
            visited[i]=True
            for j in range(n):
                if not visited[j] and M[i][j]==1:
                    dfs(j,M,visited,n)
        n=len(M)
        visited=[False for i in range(n)]
        count=0
        for i in range(n):
            if not visited[i]:
                dfs(i,M,visited,n)
                count+=1
        return count

