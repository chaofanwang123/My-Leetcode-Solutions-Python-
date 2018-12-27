import math
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==1:
            return 1
        n=math.floor((-1+math.sqrt(1+8*N))/2)
        ans=1
        for i in range(2,n+1):
            if i%2 and N%i==0:
                ans+=1
            elif i%2==0 and N%(i//2)==0 and (N//(i//2))%2:
                ans+=1
        return ans

