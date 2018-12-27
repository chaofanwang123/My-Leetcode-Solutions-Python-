from collections import defaultdict
class Solution:
    def __init__(self):
        self.d=defaultdict(list)
    def setRatio(self,x,y,ratio):
        self.d[x].append([y,ratio])
        self.d[y].append([x,1/ratio])
    def getRatio(self,x,y):
        def dfs(u,value):
            vset.add(u)
            string=[item[0] for item in self.d[u]]
            stringvalue=[item[1] for item in self.d[u]]
            for v,w in zip(string,stringvalue):
                if v==y:
                    self.ans=value*w
                    return True  
                if v not in vset:
                    if dfs(v,value*w):
                        return True
            vset.remove(u)
            return False
        if x not in self.d or not self.d[x]: return None
        vset=set()
        self.ans=None       
        dfs(x,1)
        return self.ans

obj=Solution()
obj.setRatio('a','b',0.5)
obj.setRatio('b','c',2)
result=obj.getRatio('a','c')

        

