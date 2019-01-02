class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def issub(s1,s2):
            if not set(s1)<=set(s2):
                return False
            for letter in s1:
                index=s2.find(letter)
                if index==-1:
                    return False
                s2=s2[index+1:]
            return True
            
        strs.sort(key=len)
        d={}
        for word in strs:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        if d[strs[-1]]==1:
            return len(strs[-1])
        vset=set([strs[-1]])
        n=len(strs)
        for i in range(n-2,-1,-1):
            note=0
            if d[strs[i]]==1:
                for word in vset:
                    if issub(strs[i],word):
                        note=1
                        break
                if note==0:
                    return len(strs[i])
            vset.add(strs[i])
        return -1

strs=["a","b","c","d","e","f","a","b","c","d","e","f"]
c=Solution().findLUSlength(strs)