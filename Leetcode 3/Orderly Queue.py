class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K==1:
            ans=S
            for i in range(1,len(S)):
                ans=min(ans,S[i:]+S[:i])
            return ans
        return ''.join(sorted(S))
            
