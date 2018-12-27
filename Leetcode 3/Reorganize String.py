from collections import Counter
import bisect
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n=len(S)
        d=sorted(Counter(S).items(),key=lambda x:x[1])
        if d[-1][1]>(n+1)//2:
            return ''
        
        template=''
        countlist=[]
        for letter,count in d:
            template+=letter
            countlist.append(count)
        s='##'
         
        while len(countlist)>1:
            count=countlist.pop(0)
            s=s[:-1]+template*count+s[-1]
            template=template[1:]
            for i in range(len(countlist)):
                countlist[i]-=count
            index=bisect.bisect_right(countlist,0)
            if index>0:
                countlist[:index]=[]
                template=template[index:]
                
        if len(countlist)==1:
            while countlist[0]>0:
                for i in range(1,len(s)):
                    if s[i-1]!=template and s[i]!=template:
                        s=s[:i]+template+s[i:]
                        break
                countlist[0]-=1
        return s[1:-1]

S='aab'
c=Solution().reorganizeString(S)              
            
        
