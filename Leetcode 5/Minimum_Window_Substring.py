class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s=='':
            return ''
        n=len(s)
        count=0
        d1=dict()
        for m in range(len(t)):
            if t[m] not in d1:
                d1[t[m]]=1
            else:
                d1[t[m]]+=1
        d={item:0 for item in d1}        
        countmax=len(d)
        j=0
        i=0
        length=float('inf')
        List=[]
        while j<n:
            if s[j] in d:
                d[s[j]]+=1
                if d[s[j]]==d1[s[j]]:
                    count+=1
                if count==countmax:
                    while count==countmax:
                        if s[i] in d:
                            d[s[i]]-=1
                            if d[s[i]]<d1[s[i]]:
                                count-=1
                        i+=1
                    if j-i+2<=length:
                        length=j-i+2
                        List=[i-1,j]
            j+=1
        if List==[]:
            return ''
        return s[List[0]:List[1]+1]

s = "ADOBECODEBANC"
t = "ABC"
c=Solution().minWindow(s,t)
