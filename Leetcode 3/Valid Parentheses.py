class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        str1='([{'
        str2=')]}'
        for string in s:
            if not stack or string in str1:
                stack.append(string)
            else:
                if stack.pop()[-1]!=str1[str2.index(string)]:
                    return False
        return False if stack else True

