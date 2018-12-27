import bisect
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        if n==4:
            return 4
        if n==5:
            return 5
        dp=[1,2,3,4,5]
        for i in range(5,n):
            temp1=dp[bisect.bisect_right(dp,dp[-1]/2)]*2
            temp2=dp[bisect.bisect_right(dp,dp[-1]/3)]*3
            temp3=dp[bisect.bisect_right(dp,dp[-1]/5)]*5
            dp.append(min(temp1,temp2,temp3))
        return dp[-1]

class Solution2:
    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = c = 0
        ans = [1] * n
        for i in range(1, n):
            ans[i] = min(ans[a] * 2, ans[b] * 3, ans[c] * 5)
            if ans[a] * 2 == ans[i]: 
                a += 1
            if ans[b] * 3 == ans[i]: 
                b += 1
            if ans[c] * 5 == ans[i]: 
                c += 1
        return ans[-1]


c=Solution2().nthUglyNumber2(1600)
            
        

