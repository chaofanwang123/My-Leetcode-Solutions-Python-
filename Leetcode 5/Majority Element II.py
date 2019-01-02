class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        m=n//3
        d=dict()
        ans=[]
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            if d[nums[i]]>m:
                ans.append(nums[i])
        return list(set(ans))

nums=[1]
c=Solution().majorityElement(nums)