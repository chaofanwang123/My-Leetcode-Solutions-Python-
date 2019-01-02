class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        maxl=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif stack:
                if s[stack[-1]]=='(':
                    stack.append(i)
                else:
                    while stack and s[stack[-1]]==')':
                        stack.pop() # pop ')' index
                        start=stack.pop() # pop '(' index
                    if not stack:
                        maxl=max(maxl,i-start)
                    else:
                        stack.append(i)   
        while stack:
            if s[stack[-1]]==')':
                end=stack[-1]
                while stack and s[stack[-1]]==')':
                    stack.pop() # pop ')' index
                    start=stack.pop() # pop '(' index
                maxl=max(maxl,end-start+1)
            else:
                while stack and s[stack[-1]]=='(':
                    stack.pop()
        return maxl    
    
class Solution2:
    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxans = 0
        stack = [-1]                  
        
        for i, c in enumerate(s):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i-stack[-1])
        return maxans

    
s="()(())"
c=Solution().longestValidParentheses(s)      

