class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs1(ss,step,countlist,stack1,List1,d):
            if min(countlist)<0:
                return
            if countlist[-1]==0:
                List1.append(''.join(ss))
                return
            index=stack1.pop()
            ss[index]=''
            if d[index]==len(countlist)-1:
                countlist.pop()
            else:
                for i in range(d[index]+1:len(countlist)):
                    countlist[i]-=1
                    if countlist[i]<0:
                        return
           
        if s=='':
            return ['']
        n=len(s)
        ss=list(s)
        i=0
        while i<n and ss[i]!='(':
            if ss[i]==')':
                ss[i]=''
            i+=1
        s1=''.join(ss[:i])
        if i==n:
            return [s1]
        ss=ss[i:]
        n=len(s)
        j=n-1
        while j>0 and ss[j]!=')':
            if ss[j]=='(':
                ss[j]=''
            j-=1
        s2=''.join(ss[j+1:])
        if j==0:
            return [s1+s2]
        # s[i:j+1] (...)
        s=s[i:j+1]
        countlist=[1]
        stack=['(']
        stack1=[0]
        stack2=[]
        i=1
        n=len(s)
        summ=0
        while i<n:
            if s[i]=='(':
                stack.append('(')
                stack1.append(i)
                if countlist[-1]>=0:
                    countlist.append(countlist[-1]+1)
                else:
                    countlist.append(1)
            elif s[i]==')':
                stack2.append(i)
                if stack==[] or stack[-1]!='(':
                    stack.append(')')
                    countlist.append(countlist[-1]-1)
                    summ+=countlist[-1]
                else:
                    stack.pop()
                    countlist.append(countlist[-1]-1)         
            i+=1        

        if (countlist[-1]-summ)==0:
            return [s1+s+s2]
        if summ==0:
            step=countlist[-1]
            
            
        #dfs(s,count,stack1,stack2)
        #return 
            

        
s="(a)())()"
c=Solution().removeInvalidParentheses(s)                  
            
        



