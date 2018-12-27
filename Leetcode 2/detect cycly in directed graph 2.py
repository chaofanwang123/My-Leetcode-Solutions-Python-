class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(v,d,visitedlist,backlist):
            visitedlist[v]=True
            backlist[v]=True
            if v in d:
                for u in d[v]:
                    if visitedlist[u]==False:
                        if dfs(u,d,visitedlist,backlist):
                            return True
                    elif backlist[u]:
                        return True
            visitedlist[v]=False
            backlist[v]=False
            return False
            
        d=dict()
        for a,b in prerequisites:
            if a in d:
                d[a].append(b)
            else:
                d[a]=[b]
                
        visitedlist=[False]*numCourses
        backlist=[False]*numCourses
        for v in d:
            if visitedlist[v]==False:
                if dfs(v,d,visitedlist,backlist):
                    return False
        return True
                
numCourses=2
prerequisites=[[1,0]]
c=Solution().canFinish(numCourses,prerequisites)
