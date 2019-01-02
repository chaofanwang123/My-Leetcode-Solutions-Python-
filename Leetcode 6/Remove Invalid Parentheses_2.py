class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs2(ss,count1,count2,stack2,List2):
            if count1==0:
                List2.add(ss)
                return
            if count2==0:
                for i in range(len(stack2)-1,-1,-1):
                    ss=ss[:stack2[i]]+ss[stack2[i]+1:]
                List2.add(ss)
                return
            dfs2(ss,count1,count2-1,stack2[:-1],List2)
            dfs2(ss[:stack2[-1]]+ss[stack2[-1]+1:],count1-1,count2,stack2[:-1],List2)
            
        if s=='':
            return ['']
        n=len(s)
        ss=list(s)
        i=0
        while i<n and ss[i]!='(':
            if ss[i]==')':
                ss[i]=''
            else:
                i+=1
        s1=''.join(ss[:i])
        if i==n:
            return [s1]
        s=s[i:]
        n=len(s)
        stack1=[0]
        i=1
        stack2=[]
        count=1
        while i<n and count>=0:
            if s[i]=='(':
                count+=1
                stack1.append(i)
            elif s[i]==')':
                count-=1
                stack2.append(i)
            i+=1
        if count==-1:
            #check '(' or ')' after count==0
            while i<n:
                if s[i]==')':
                    count-=1
                    stack2.append(i)
                elif s[i]=='(':
                    # count<0, remove any -count ')' from stack2
                    m=len(stack2)
                    List2=set([])
                    dfs2(s[:i],-count,m+count,stack2,List2)
                    a1=[s1+item1 for item1 in List2]
                    b1=self.removeInvalidParentheses(s[i:])
                    List=[]
                    for i in a1:
                        for j in b1:
                           List.append(s1+i+j) 
                    return List
                i+=1
            List2=set([])
            m=len(stack2)
            dfs2(s[:i],-count,m+count,stack2,List2)
            List=[]
            for item1 in List2:
                List+=self.removeInvalidParentheses(s1+item1)
            return List
        elif count==0: # count>=0
            return [s1+s]
        else:
            s=s1+s
            ss=list(s)
            for i in range(len(ss)):
                if ss[i]=='(':
                    ss[i]=')'
                elif ss[i]==')':
                    ss[i]='('
            s=''.join(ss)
            a1=self.removeInvalidParentheses(s[::-1])
            for i in range(len(a1)):
                item=list(a1[i])
                for j in range(len(item)):
                    if item[j]=='(':
                        item[j]=')'
                    elif item[j]==')':
                        item[j]='('
                item=''.join(item)
                a1[i]=item[::-1]
            return a1
        
s="(((()(()" #output=["()()","(())"]
c=Solution().removeInvalidParentheses(s)                  
            
        

