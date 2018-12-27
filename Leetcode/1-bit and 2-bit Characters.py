class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n=len(bits)
        if n==1 or bits[-2]==0:
            return True
        if n==2:
            return False
        dp0=True
        dp1=True if bits[0]==0 else False
        for i in range(2,n-1):
            dp2=(dp1 and bits[i-1]==0) or (dp0 and (bits[i-2:i]==[1,0] or bits[i-2:i]==[1,1]))
            dp0,dp1=dp1,dp2
        return not dp1

bits=[1,0,0,1,0]
c=Solution().isOneBitCharacter(bits)