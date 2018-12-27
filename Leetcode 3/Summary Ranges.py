class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        n=len(nums)
        if n==1:
            return [str(nums[0])]
        ans=[]
        start=nums[0]
        i=1
        while i<n:
            while i<n and nums[i]==nums[i-1]+1:
                i+=1
            if nums[i-1]==start:
                ans.append(str(start))
            else:
                ans.append(str(start)+'->'+str(nums[i-1]))
            if i<n:
                start=nums[i]
                i+=1
                if i==n:
                    ans.append(str(start))
        return ans

nums=[0,1]
c=Solution().summaryRanges(nums)