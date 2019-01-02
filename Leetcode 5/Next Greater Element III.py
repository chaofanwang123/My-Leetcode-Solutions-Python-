class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        List=[int(i) for i in str(n)]
        i=len(List)-2
        while i>=0 and List[i]>=List[i+1]:
            i-=1
        if i>=0:
            j=i+2
            while j<len(List) and List[j]>List[i]:
                j+=1
            List[i],List[j-1]=List[j-1],List[i]
            s=''.join(str(item) for item in List)
            num=int(s[:i+1]+s[len(s)-1:i:-1])
            return num if num<2**31 else -1
            
        return -1

n=1999999999
c=Solution().nextGreaterElement(n)