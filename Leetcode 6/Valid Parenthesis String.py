class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        lastindex=[]
        for string in s:
            if string=='*':
                stack.append(string)
            elif string=='(':
                lastindex.append(len(stack))
                stack.append(string)
            else:
                if not stack:
                    return False
                if lastindex:
                    del stack[lastindex.pop()]
                else:
                    stack.pop()
        if not stack:
            return True
        
        stack1=[]
        for string in stack:
            if string=='(':
                stack1.append(string)
            else:
                if stack1:
                    stack1.pop()
        return not stack1

s="((*)))"
c=Solution().checkValidString(s)
