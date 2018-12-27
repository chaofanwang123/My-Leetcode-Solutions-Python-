class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        if n==1:
            return 1
        maxl=[0]*n
        minr=[0]*n
        maxl[0]=arr[0]
        minr[n-1]=arr[n-1]
        for i in range(1,n):
            maxl[i]=max(maxl[i-1],arr[i])
            minr[n-1-i]=min(minr[n-i],arr[n-1-i])
        count=0
        i=n-1
        while i>=0:
            j=i
            while j>0 and maxl[j-1]>minr[j]:
                j-=1
            count+=1
            i=j-1
        return count

arr = [2,1,3,4,4]
c=Solution().maxChunksToSorted(arr)