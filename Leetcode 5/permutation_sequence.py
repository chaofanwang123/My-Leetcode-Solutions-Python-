class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=[m+1 for m in range(n)]
        i=1
        List=[]
        k=k-1
        while k>=1:
            i+=1
            List.insert(0,k%i)
            k=k//i
        templist=[mm+n-i+1 for mm in range(i)]
        List.append(0)
        for j in range(i):
            s[n-i+j]=templist.pop(List[j])
        return ''.join(str(ss) for ss in s )

n=3
k=1
c=Solution().getPermutation(n,k)
        

