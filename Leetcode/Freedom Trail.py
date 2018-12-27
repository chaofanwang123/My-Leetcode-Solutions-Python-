#from collections import defaultdict
#class Solution2:
#    def findRotateSteps2(self, ring, key):
#        """
#        :type ring: str
#        :type key: str
#        :rtype: int
#        """
#        def dfs(index,key,count):
#            if key=='':
#                self.min=min(self.min,count)
#                return
#            key1=key[0]
#            for i in d[key1]:
#                step=abs(i-index)
#                step=min(step,n-step)
#                dfs(i,key[1:],count+step+1)
#        d=defaultdict(list)
#        n=len(ring)
#        for i in range(n):
#            d[ring[i]].append(i)
#        self.min=float('inf')
#        dfs(0,key,0)
#        return self.min

from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        d=defaultdict(list)
        n=len(ring)
        for i in range(n):
            d[ring[i]].append(i)
        m=len(key)
        dp=[[0,0]]
        for i in range(m):
            temp=[]
            for index in d[key[i]]:
                mincount=float('inf')
                for count,loc in dp:
                    step=abs(loc-index)
                    step=min(step,n-step)
                    count+=step
                    if count<mincount:
                        mincount=count
                temp.append([mincount+1,index])
            dp=temp
        minstep=float('inf')
        for i in dp:
            minstep=min(minstep,i[0])
        return minstep
                    
ring = "caotmcaataijjxi"
key="oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"       
#ring = "godding"
#key = "gd"
c=Solution().findRotateSteps(ring,key)            
    

