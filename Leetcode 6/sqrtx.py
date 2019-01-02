class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        left=1
        right=int(x/2)+1
        while left<=right:
            mid=(left+right)//2
            mid2=mid*mid
            if mid2==x:
                return mid
            elif mid2<x:
                left=mid+1
            else:
                right=mid-1
        return right

c=Solution().mySqrt(9)

