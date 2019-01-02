class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidParentheses(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                elif i == ')':
                    if count == 0: 
                        return False
                    count -= 1
            return count == 0
        if not s: return ['']
        q=[s]
        List=[]
        vis=set([s])
        found = False
        while q:
            cur = q.pop(0)
            if isValidParentheses(cur):
                found = True
                List.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return List

class Solution2:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def removeInvalidParensHelp(s, count, i, j, rev=False):
            ans = []
            while j < len(s):
                if s[j] == '(':
                    count += 1
                elif s[j] == ')':
                    if count == 0:
                        while i <= j:
                            if s[i] == ')' and (i-1 < 0 or s[i-1] != ')'):
                                ans += removeInvalidParensHelp(s[:i]+s[i+1:],count, i, j, rev)
                            i += 1
                        return ans
                    else:
                        count -= 1
                j += 1
                        
            if not rev:
                return removeInvalidParensHelp(s[::-1], 0, 0, 0, True)
            else:
                return [s[::-1]]
                    
        return removeInvalidParensHelp(s, 0, 0, 0)
    
s="(a)())()"
c=Solution().removeInvalidParentheses(s)     
