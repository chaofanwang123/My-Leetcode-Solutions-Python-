import math
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(s,L):
            if len(s)==(L+1)//2:
                num=int(s[:-1]+s[::-1])
                if num<N:
                    return False
                for divisor in range(3,math.floor(math.sqrt(num))+1,2):
                    if num%divisor==0:
                        return False
                self.ans=num
                return True
            for newdigit in '0123456789':
                if (L>length or L==length and s+newdigit>=Ns[:len(s)+1]) and dfs(s+newdigit,L):
                    return True
            return False
        
        Ns=str(N)
        length=len(Ns)
        
        if length<=2:
            for num in [2,3,5,7,11,101]:
                if num>=N:
                    return num
                
        self.ans=None
        if length%2==0:
            for L in range(length+1,10,2):
                for digit1 in '13579':
                    if dfs(digit1,L):
                        return self.ans
        else:
            for L in range(length,10,2):
                for digit1 in '13579':
                    if dfs(digit1,L):
                        return self.ans

N=10502
c=Solution().primePalindrome(N)