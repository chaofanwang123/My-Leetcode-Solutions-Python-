from collections import defaultdict
class Solution2:
    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d1=defaultdict(set)
        d2=defaultdict(set)
        for u,v in prerequisites:
            d1[u].add(v)
            d2[v].add(u)
        while True:
            for v in d2:
                if v not in d1:
                    for u in d2[v]:
                        d1[u].remove(v)
                        if not d1[u]:
                            del d1[u]
                    del d2[v]
class Solution3:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish3(self, numCourses, prerequisites):
        if numCourses<2 or len(prerequisites)<2:
            return True
        #prerequisites.sort()
        while True:
            count=0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False
            for pre in prerequisites:
                if mark[pre[1]]:
                    count+=1
                    prerequisites.remove(pre)
            if prerequisites==[]:
                return True
            elif count==0:
                return False

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for i, j in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

numCourses=2
prerequisites=[[1,0],[0,1]]
c=Solution().canFinish(numCourses,prerequisites)