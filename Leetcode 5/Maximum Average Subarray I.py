class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        if n==k:
            return sum(nums)/k
        temp=sum(nums[:k])
        maxv=temp
        for i in range(k,n):
            temp+=nums[i]-nums[i-k]
            maxv=max(maxv,temp)
        return maxv/k

