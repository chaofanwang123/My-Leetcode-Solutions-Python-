class Solution2:
    def findSubsequences2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        if n<2:
            return []
#        i=1
#        while i<n and nums[i]<nums[i-1]:
#            i+=1
#        if i==n:
#            return []
        dp=[]
        for i in range(n):
            m=len(dp)
            for j in range(m):
                if dp[j][-1]<=nums[i]:
                    temp=dp[j]+[nums[i]]
                    if temp not in dp:
                        dp.append(temp)
            for j in range(i):
                if nums[j]<=nums[i] and [nums[j],nums[i]] not in dp:
                    dp.append([nums[j],nums[i]])
        return dp

class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        if n<2:
            return []
        dp=set([])
        for i in range(1,n):
            temp=set([])
            for j in range(i):
                if nums[i]>=nums[j]:
                    temp.add((nums[j],nums[i]))
            for item in dp:
                if nums[i]>=item[-1]:
                    temp.add(tuple(list(item)+[nums[i]]))
            dp.update(temp)
        return [list(item) for item in dp]
    
nums=[-96,-97,-98,-99,-99]
c=Solution().findSubsequences(nums)
