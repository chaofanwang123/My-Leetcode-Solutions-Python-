class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1=='':
            return s2==s3
        if s2=='':
            return s1==s3
        n1,n2,n3=len(s1),len(s2),len(s3)
        if n1+n2!=n3:
            return False
        stemp=s1+s2
        d1,d2={},{}
        for i in range(n3):
            if stemp[i] not in d1:
                d1[stemp[i]]=1
            else:
                d1[stemp[i]]+=1
            if s3[i] not in d2:
                d2[s3[i]]=1
            else:
                d2[s3[i]]+=1
        for item in d1:
            if item not in d2 or d1[item]!=d2[item]:
                return False
        dp=[[False for j in range(n2+1)] for i in range(n1+1)]
        dp[0][0]=True
        for i in range(n1+1):
            for j in range(n2+1):
                if dp[i][j]:
                    if i<n1 and s1[i]==s3[i+j]:
                        dp[i+1][j]=True
                    if j<n2 and s2[j]==s3[i+j]:
                        dp[i][j+1]=True
                        
        return dp[-1][-1]
                
        

s1 = "aa"
s2 = "ab"
s3 = "abaa"
c=Solution().isInterleave(s1,s2,s3)