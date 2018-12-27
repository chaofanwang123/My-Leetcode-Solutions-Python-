from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u,d,vlist,stack,backlist):
            vlist[u]=True
            backlist[u]=True
            for i in d[u]:
                if vlist[i]==False:
                    if dfs(i,d,vlist,stack,backlist):
                        return True
                elif backlist[i]:
                    return True
            backlist[u]=False
            stack.insert(0,u)
            return False
        
        if prerequisites==[]:
            return [i for i in range(numCourses)]
        d=defaultdict(list)
        for u,v in prerequisites:
            d[v].append(u)
        vlist=[False]*numCourses
        backlist=[False]*numCourses
        stack=[]
        for i in range(numCourses):
            if vlist[i]==False:
                if dfs(i,d,vlist,stack,backlist):
                    return []
        return stack
                
prerequisites=[[1,0]]
numCourses=3
c=Solution().findOrder(numCourses,prerequisites)
            

