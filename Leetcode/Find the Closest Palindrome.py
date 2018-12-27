class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        m=len(n)
        if m==1:
            return str(int(n)-1)
        List=['1'+'0'*(m-1)+'1','9'*(m-1)]
        s=n[:(m+1)//2]
        s1,s2=str(int(s)-1),str(int(s)+1)
        if m%2:
            List+=[s+s[:-1][::-1],s1+s1[:-1][::-1],s2+s2[:-1][::-1]]
        else:
            List+=[s+s[::-1],s1+s1[::-1],s2+s2[::-1]]
        
        ans=List.pop(0)
        minv=abs(int(n)-int(ans))
        for string in List:
            if string!=n and string[0]!='0':
                dif=abs(int(n)-int(string))
                if dif<minv:
                    minv=dif
                    ans=string
                elif dif==minv:
                    ans=str(min(int(ans),int(string)))
        return ans
            

