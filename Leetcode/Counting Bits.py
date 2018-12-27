class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0:
            return [0]
        if num==1:
            return [0,1]
        dp=[0]
        num1=num
        count=0
        while num>=2:
            count+=1
            num=num//2
            temp=[i+1 for i in dp]
            dp+=temp
        rem=num1-pow(2,count)
        temp=[dp[i]+1 for i in range(rem+1)]
        return dp+temp

c=Solution().countBits(5)
