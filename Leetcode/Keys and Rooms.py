class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            visited[i]=True
            for item in rooms[i]:
                if not visited[item]:
                    dfs(item)
        n=len(rooms)
        visited=[False for i in range(n)]
        dfs(0)
        return visited==[True]*n
rooms=[[1,3],[3,0,1],[2],[0]]
c=Solution().canVisitAllRooms(rooms)

