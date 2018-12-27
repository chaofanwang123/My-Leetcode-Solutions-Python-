class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        count=R*C-1
        ans=[[r0,c0]]
        cur=[r0,c0,0] # 0,1: East,West
        step=1
        while count>0:
            if cur[2]==0: # East
                if 0<=cur[0]<R:
                    for j in range(1,step+1):
                        if 0<=cur[1]+j<C:
                            ans.append([cur[0],cur[1]+j])
                            count-=1
                cur[1]+=step
                if 0<=cur[1]<C:
                    for j in range(1,step+1):
                        if 0<=cur[0]+j<R:
                            ans.append([cur[0]+j,cur[1]])
                            count-=1
                cur[0]+=step
                cur[2]=1
                step+=1
            else:
                if 0<=cur[0]<R:
                    for j in range(1,step+1):
                        if 0<=cur[1]-j<C:
                            ans.append([cur[0],cur[1]-j])
                            count-=1
                cur[1]-=step
                if 0<=cur[1]<C:
                    for j in range(1,step+1):
                        if 0<=cur[0]-j<R:
                            ans.append([cur[0]-j,cur[1]])
                            count-=1
                cur[0]-=step
                cur[2]=0
                step+=1
        return ans
                
R = 1
C = 4
r0 = 0
c0 = 0   
c=Solution().spiralMatrixIII(R,C,r0,c0)             
                
            

