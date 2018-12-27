class Solution2:
    def integerReplacement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n % 2:
            return min(self.integerReplacement2(n-1), self.integerReplacement2(n+1)) +1
        else:
            return self.integerReplacement2(n//2) + 1
n=160
c=Solution2().integerReplacement2(n)        

