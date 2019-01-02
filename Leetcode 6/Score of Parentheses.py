class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack=[]
        for s in S:
            if s=='(':
                stack.append(s)
            else:
                tempscore=0
                while stack[-1]!='(':
                    tempscore+=stack.pop()
                stack[-1]=tempscore*2 if tempscore!=0 else 1
        return sum(stack)
                    
S="(()(()))"
c=Solution().scoreOfParentheses(S)

