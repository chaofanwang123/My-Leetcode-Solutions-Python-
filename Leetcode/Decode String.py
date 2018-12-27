class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def dfs(s,List):
            
        if s==[]:
            return []
        List=[]
        stack=[]
        i=0
        n=len(s)
        while i<n:
            if s[i]!='[' or s[i]!=']':
                List.append(i)
            elif s[i]=='[':
                stack.append(i)
            elif s[i]==']':

