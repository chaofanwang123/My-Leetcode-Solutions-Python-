class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s==[]:
            return []
        if len(s)==1:
            return s
        if numRows==1:
            return s
        T=2*(numRows-1)
        n=len(s)
        m=n//T
        r=n%T
        sout=[0]*n
        if r==0:
            for i in range(numRows):
                if i==0:
                    for j in range(m):
                        sout[j]=s[j*T]
                elif i==numRows-1:
                    for j in range(m):
                        sout[n-m+j]=s[i+j*T]
                else:
                    index=m+(i-1)*2*m
                    for j in range(m):    
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T]
        elif r<numRows:
            for i in range(r):
                if i==0:
                    for j in range(m+1):
                        sout[j]=s[j*T]
                else:
                    index=m+1+(i-1)*(2*m+1)
                    for j in range(m):
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T]
                    sout[index+2*m]=s[i+m*T]
            for i in range(r,numRows):
                if i==numRows-1:
                    index=n-m
                    for j in range(m):
                        sout[index+j]=s[i+j*T]
                else:
                    index=m+1+(r-1)*(2*m+1)+(i-r)*2*m
                    for j in range(m):
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T]
                
        elif r==numRows:
            for i in range(r):
                if i==0:
                    for j in range(m+1):
                        sout[j]=s[j*T]
                elif i==numRows-1:
                    index=m+1+(i-1)*(2*m+1)
                    for j in range(m+1):
                        sout[index+j]=s[i+j*T]         
                else:
                    index=m+1+(i-1)*(2*m+1)
                    for j in range(m):
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T]
                    sout[index+2*m]=s[i+m*T]
                    
        else:
            for i in range(T-r+1):
                if i==0:
                    for j in range(m+1):
                        sout[j]=s[j*T]
                else:
                    index=m+1+(i-1)*(2*m+1)
                    for j in range(m):
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T]
                    sout[index+2*m]=s[i+m*T]            
            for i in range(T-r+1,numRows):
                if i==numRows-1:
                    index=n-m-1
                    for j in range(m+1):
                        sout[index+j]=s[i+j*T]
                else:
                    index=m+1+(T-r)*(2*m+1)+(i-(T-r+1))*(2*m+2)
                    for j in range(m+1): 
                        sout[index+j*2]=s[i+j*T]
                        sout[index+j*2+1]=s[T-i+j*T] 
        return ''.join(sout)

        

