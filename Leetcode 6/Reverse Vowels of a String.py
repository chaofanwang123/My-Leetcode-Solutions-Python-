class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        string='aeiouAEIOU'
        List=[]
        for i in range(len(s)):
            if s[i] in string:
                List.append(i)
        n=len(List)
        if n<=1:
            return s
        s=list(s)
        for i in range(n//2):
            s[List[i]],s[List[n-1-i]]=s[List[n-1-i]],s[List[i]]
        return ''.join(s)