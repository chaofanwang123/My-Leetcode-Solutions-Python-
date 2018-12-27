class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digitset=set('0125698')
        dset=set('2569')
        count=0
        for i in range(1,N+1):
            temp=set(str(i))
            if temp<=digitset and temp&dset:
                count+=1
        return count

N=2
c=Solution().rotatedDigits(N)
                
                
        
            
        

