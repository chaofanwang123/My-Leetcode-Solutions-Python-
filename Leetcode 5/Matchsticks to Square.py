class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def bfs(i,d,summ,visited):
            visited[i]=True
            if summ in d and d[summ]>0:
                d[summ]-=1
                return True
            
        
        if len(nums)<4:
            return False
        sumall=sum(nums)
        if sumall%4!=0:
            return False
        side=sumall//4
        nums.sort()
        stack=nums[-1]
        visited=[False]*len(nums)
        
        
