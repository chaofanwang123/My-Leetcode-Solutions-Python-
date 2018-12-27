import math
from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s=str(N)
        n=len(s)
        if n==1:
            return N==1 or N==2 or N==4 or N==8
        minN,maxN=int('1'+'0'*(n-1)),int('9'*n)
        min_pow,max_pow=math.ceil(math.log2(minN)),math.floor(math.log2(maxN))
        d=Counter(s)
        for i in range(min_pow,max_pow+1):
            if Counter(str(pow(2,i)))==d:
                return True
        return False

