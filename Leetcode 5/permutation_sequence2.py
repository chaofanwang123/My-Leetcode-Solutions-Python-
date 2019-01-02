
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
        while k>1:
            k=k//i
            i+=1
            List.insert(0,k%i)
        i-=1
        templist=[mm+n-i+1 for mm in range(i)]
        for j in range(i):
            s[n-i+j]=templist.pop(List[j])
        return s

n=3
k=4
c=Solution().getPermutation(n,k)
        



