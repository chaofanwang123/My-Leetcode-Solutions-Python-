class Solution2(object):
    def findLongestChain2(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n=len(pairs)
        if n<=1:
            return n
        pairs.sort(key=lambda x:x[1])
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if pairs[j][1]>=pairs[i][0]:
                    break
                dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        if not pairs: return 0
        pairs.sort(key=lambda x:x[1])
        
        res=0
        end=-2**32
        for pair in pairs:
            if pair[0]>end:
                res+=1
                end=pair[1]
        return res
    
pairs=[[1,2], [2,3], [3,4]]
c=Solution().findLongestChain(pairs)
