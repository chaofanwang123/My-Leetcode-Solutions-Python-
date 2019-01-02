import numpy as np
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%4==0:
            n=n//4
        stack=[n]
        vset=set()
        count=0
        while True:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                num=stack.pop(0)
                i=int(np.sqrt(num))
                if i**2==num:
                    return count
                for k in range(i,0,-1):
                    temp=num-k**2
                    if temp not in vset:
                        vset.add(temp)
                        stack.append(temp)
        return count
class Solution2:
    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """        
        while n & 3 == 0: # n % 4 == 0
            n >>= 2
        if n & 7 == 7: # n % 8 == 7
            return 4
        r = n ** 0.5
        if r == int(r):
            return 1
        a = 1
        limit = n // 2
        while a * a <= limit:
            b = int((n - a * a) ** 0.5)
            if a * a + b * b == n:
                return 2
            a = a + 1
        return 3
n=13
c=Solution().numSquares(n)
            
        

