class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        i=len(s)-1
        string='0123456789'
        while i>=0:
            if s[i] in string:
                j=i-1
                while j>=0 and s[j] in string:
                    s[i]=s[j]+s[i]
                    s[j]=''
                    j-=1
                i=j
            i-=1
        i=len(s)-1
        while i>=0:
            if s[i]==' ' or s[i]=='':
                del s[i]
            i-=1
        i=1
        ans=0
        while i<len(s)-1:
            if s[i]=='*':
                temp=int(s[i-1])*int(s[i+1])
                s[i+1]=str(temp)
                s[i-1],s[i]='',''
            elif s[i]=='/':
                temp=int(s[i-1])//int(s[i+1])
                s[i+1]=str(temp)
                s[i-1],s[i]='',''
            i+=2
        i=len(s)-1
        while i>=0:
            if s[i]=='':
                del s[i]
            i-=1
        i=1
        ans=int(s[0])
        for i in range(1,len(s)-1,2):
            if s[i]=='+':
                ans+=int(s[i+1])
            else:
                ans-=int(s[i+1])
        return ans
            
s="12-3*4"      
c=Solution().calculate(s)