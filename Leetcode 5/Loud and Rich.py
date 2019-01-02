from collections import defaultdict
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        def dfs(i):
            if visited[i]!=-1:
                return visited[i]
            if d[i]==[]:
                visited[i]=i
                return visited[i]
            minv=quiet[i]
            y=i
            for person in d[i]:
                x=dfs(person)
                if quiet[x]<minv:
                    minv=quiet[x]
                    y=x
            visited[i]=y
            return y
        d=defaultdict(list)
        for item in richer:
            d[item[1]].append(item[0])
        visited=[-1 for i in range(len(quiet))]
        for i in range(len(quiet)):
            if visited[i]==-1:
                dfs(i)
        return visited

richer = []
quiet = [0]
c=Solution().loudAndRich(richer,quiet)
