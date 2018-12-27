class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def addbinary(a,b,m,n):
            c=''
            over=0
            for i in range(m):
                digit=int(a[m-1-i])+int(b[n-1-i])+over
                over=digit//2
                digit=digit%2
                c=str(digit)+c
            for j in range(n-m):
                digit=int(b[n-m-1-j])+over
                over=digit//2
                digit=digit%2
                c=str(digit)+c
            if over==1:
                c='1'+c
            return c
        m=len(a)
        n=len(b)
        if m==0:
            return b
        if n==0:
            return a
        if m<=n:
            return addbinary(a,b,m,n)
        return addbinary(b,a,n,m)
