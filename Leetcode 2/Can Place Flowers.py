class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return True
        i=0
        m=len(flowerbed)
        while i<m and flowerbed[i]==0:
            i+=1
        n-=i//2 if i<m else (i+1)//2
        if n<=0:
            return True
        while i<m:
            if flowerbed[i]==1:
                i+=1
                while i<m and flowerbed[i]==1:
                    i+=1
                if i==m:
                    return False
                j=i
                while j<m and flowerbed[j]==0:
                    j+=1
                step=j-i
                n-=(step-1)//2 if j<m else step//2
                if n<=0:
                    return True
                i=j
            else:
                i+=1
        return False
                
flowerbed = [0]
n = 1
c=Solution().canPlaceFlowers(flowerbed,n)