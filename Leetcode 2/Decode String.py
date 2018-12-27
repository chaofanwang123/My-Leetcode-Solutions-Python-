class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def dfs(s,j,d):
            List=''
            k=''
            while True:
                if s[j]==']':
                    return (List,j)
                if s[j]=='[':
                    string,endindex=dfs(s,j+1,d)
                    List=List+string*int(k)
                    j=endindex
                    k=''
                elif s[j] not in d:
                    List=List+s[j]
                else:
                    k+=s[j]
                j+=1
        s='['+s+']'
        d=('0','1','2','3','4','5','6','7','8','9')
        return dfs(s,1,d)[0]
                
s = ""     
c=Solution().decodeString(s)