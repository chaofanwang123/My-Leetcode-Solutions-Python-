class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if not stations:
            return -1 if startFuel<target else 0
        if startFuel<stations[0][0]:
            return -1
        stations.append([target,0])
        n=len(stations)
        dp=[[-float('inf')]*n for i in range(n)]
        dp[0][0]=startFuel-stations[0][0]
        dist=[stations[j][0]-stations[j-1][0] for j in range(1,n)]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]-dist[j-1]
            if dp[0][j]<0:
                break
        if dp[0][-1]>=0:
            return 0
        for i in range(1,n):
            dp[i][i]=dp[i-1][i-1]+stations[i-1][1]-dist[i-1]
            if dp[i][i]<0:
                return -1
        for i in range(1,n):
            for j in range(i+1,n):
                dp[i][j]=dp[i][j-1]-dist[j-1]
                if dp[i-1][j-1]>=0:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-1]+stations[j-1][1]-dist[j-1])
                if dp[i][j]<0:
                    break
            if dp[i][n-1]>=0:
                return i
        return -1

target = 1000
startFuel = 299
stations =[[13,100],[25,117],[122,82],[189,123],[268,56],[382,214],[408,280],[421,272],[589,110],[899,4]]
c=Solution().minRefuelStops(target,startFuel,stations)