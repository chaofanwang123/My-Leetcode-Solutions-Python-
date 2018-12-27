from collections import defaultdict
class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        def bfs(start,end):
            vset=set()
            stack=[start]
            vset.add(start)
            count=0
            while stack:
                n=len(stack)
                count+=1
                while n>0:
                    n-=1
                    u=stack.pop(0)
                    if u in d:
                        for v in d[u]:
                            if v==end:
                                return count
                            if v not in vset:
                                vset.add(v)
                                stack.append(v)
            return -1
                        
        m=len(forest)
        n=len(forest[0])
        if not forest or forest[0][0]==0:
            return -1
        d=defaultdict(list)
        for i in range(m):
            for j in range(n):
                if forest[i][j]==0:
                    continue
                note=0
                if i+1<m and forest[i+1][j]!=0:
                    d[forest[i][j]].append(forest[i+1][j])
                    note+=1
                if i-1>=0 and forest[i-1][j]!=0:
                    d[forest[i][j]].append(forest[i-1][j])
                    note+=1
                if j+1<n and forest[i][j+1]!=0:
                    d[forest[i][j]].append(forest[i][j+1])
                    note+=1
                if j-1>=0 and forest[i][j-1]!=0:
                    d[forest[i][j]].append(forest[i][j-1])
                    note+=1
                if note==0:
                    return -1
        value=sorted(d.keys())
        if forest[0][0]==value[0]:
            count=0
        else:
            count=bfs(forest[0][0],value[0])
            if count==-1:
                return -1
        for i in range(len(value)-1):
            temp=bfs(value[i],value[i+1])
            if temp==-1:
                return -1
            count+=temp
        return count

class Solution2:
    # maze (BFS) method to get min steps from A to B with obstacles
    def cutOffTree2(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                for i, row in enumerate(forest)
                for j, height in enumerate(row)
                if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))
      
forest=[[2,3,4],[0,0,5],[8,7,6]]
c=Solution().cutOffTree(forest)
