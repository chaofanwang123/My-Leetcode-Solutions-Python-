class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countnumber(nums,value):
            count=0
            start=0
            for i in range(1,n):
                if nums[i]-nums[start]<=value:
                    count+=i-start
                else:
                    while nums[i]-nums[start]>value:
                        start+=1
                    count+=i-start
            return count
        nums.sort()
        right=nums[-1]-nums[0]
        left=right
        n=len(nums)
        for i in range(1,n):
            left=min(left,nums[i]-nums[i-1])
        if k==1:
            return left
        while left<right:
            mid=(left+right)//2
            count=countnumber(nums,mid)
            if count<k:
                left=mid+1
            else:
                right=mid
        return right
nums = [1,2,3,3,14,6,8,9,10,20,100,34,59,68]
k = 10
c=Solution().smallestDistancePair(nums,k)