class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        def helper(target):
            if target in memo:
                return memo[target]
            n=target.bit_length()
            if 2**n-1==target:
                memo[target]=n
            else:
                memo[target]=helper(2**n-1-target)+n+1
                for m in range(n-1):
                    memo[target]=min(memo[target],helper(target-2**(n-1)+2**m)+n+m+1)
            return memo[target]
        memo={1:1}
        return helper(target)
        
c=Solution().racecar(33)