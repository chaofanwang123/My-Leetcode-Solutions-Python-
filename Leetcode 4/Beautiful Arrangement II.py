class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k>n-1:
            return []
        List=[i for i in range(n)]
        k-=1
        if k%2==0:
            List=[0]*k+[i for i in range(k//2+1,n-k//2+1)]
            for i in range(k//2):
                List[i*2]=i+1
                List[i*2+1]=n-i
        else:
            List=[0]*k+[i for i in range(k//2+1,n-k//2)]
            List[0]=n
            for i in range(k//2):
                List[i*2+2]=n-i-1
                List[i*2+1]=i+1
        return List

c=Solution().constructArray(5,2)
