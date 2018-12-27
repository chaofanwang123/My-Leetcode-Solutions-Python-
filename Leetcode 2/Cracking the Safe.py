class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n==1:
            ans=''
            for i in range(k):
                ans+=str(i)
            return ans
        ans = '0' * (n - 1)
        passwords = set()
        for x in range(k ** n):
            current=ans[-n+1:]
            for y in range(k - 1, -1, -1):
                if current + str(y) not in passwords:
                    passwords.add(current + str(y))
                    ans += str(y)
                    break
        return ans

n=1
k=9
c=Solution().crackSafe(n,k)