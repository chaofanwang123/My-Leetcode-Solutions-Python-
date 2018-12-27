class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        x,y=sum(A),sum(B)
        dif=(x-y)/2
        B=set(B)
        for a in A:
            if a-dif in B:
                return [a,int(a-dif)]

