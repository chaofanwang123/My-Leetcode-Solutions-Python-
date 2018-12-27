class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def dfs(index,laststep):
            if abs(stones[-1]-stones[index]-laststep)<=1:
                return True
            if laststep==1:
                if stones[index]+1 in d and (d[stones[index]+1],1) not in vset:
                    vset.add((d[stones[index]+1],1))
                    if dfs(d[stones[index]]+1,1):
                        return True
                if stones[index]+2 in d and (d[stones[index]+2],2) not in vset:
                    vset.add((d[stones[index]+2],2))
                    if dfs(d[stones[index]+2],2):
                        return True
            else:
                for u in [laststep-1,laststep,laststep+1]:
                    if stones[index]+u in d and (d[stones[index]+u],u) not in vset:
                        vset.add((d[stones[index]+u],u))
                        if dfs(d[stones[index]+u],u):
                            return True
            return False
        n=len(stones)
        if stones[1]!=1:
            return False
        d={}
        for i in range(n):
            d[stones[i]]=i
        vset=set()
        return dfs(1,1)
        

stones=[0,1,3,5,6,8,12,17]
c=Solution().canCross(stones)