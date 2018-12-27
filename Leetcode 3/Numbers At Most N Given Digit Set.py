class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        if not D:
            return 0
        D=[int(i) for i in D]
        m=len(D) 
        digits=[]
        while N>0:
            digits.insert(0,N%10)
            N=N//10
        L=len(digits)
        count=1 if set(digits)<=set(D) else 0
        factor=1
        for i in range(1,L):
            factor*=m
            count+=factor
        while digits:
            digit=digits.pop(0)
            j=0
            while j<m and D[j]<digit:
                j+=1
            if j==0:
                if D[0]>digit:
                    return count%(pow(10,9)+7)
                factor=factor//m
                continue
            if j==m:
                return (count+m*factor)%(pow(10,9)+7)
            if D[j]>digit:
                return (count+j*factor)%(pow(10,9)+7)
            count+=j*factor
            factor=factor//m
        
        return count%(pow(10,9)+7)
                
D = ["3","4","8"]
N = 4 
c=Solution().atMostNGivenDigitSet(D,N)                
        
        

