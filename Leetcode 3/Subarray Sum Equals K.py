class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        count=0
        d={0:1}
        if nums[0]-k in d:
            count+=d[nums[0]-k]
        if nums[0] not in d:
            d[nums[0]]=1
        else:
            d[nums[0]]+=1
        
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            if nums[i]-k in d:
                count+=d[nums[i]-k]
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        return count

nums=[1,2,3]
k=3
c=Solution().subarraySum(nums,k)