class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0
        if m<3 or n<3:
            return 0

        peak = [[float('inf')] * n for i in range(m)]
        stack = []
        for j in range(n):
            peak[0][j]=heightMap[0][j]
            peak[m-1][j]=heightMap[m-1][j]
            stack+=[[0,j],[m-1,j]]
        for i in range(1,m-1):
            peak[i][0]=heightMap[i][0]
            peak[i][n-1]=heightMap[i][n-1]
            stack+=[[i,0],[i,n-1]]

        while stack:
            x, y = stack.pop(0)
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if 1<=nx<=m-2 and 1<=ny<=n-2:
                    limit = max(peak[x][y], heightMap[nx][ny])
                    if peak[nx][ny] > limit:
                        peak[nx][ny] = limit
                        stack.append((nx, ny))

        return sum(peak[x][y] - heightMap[x][y] for x in range(m) for y in range(n))
                    

heightMap=[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
c=Solution().trapRainWater(heightMap)