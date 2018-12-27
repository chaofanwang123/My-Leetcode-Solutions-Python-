class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        if n==1:
            return 0
        if n%2:
            k=(n+1)//2
            return nums[k-1]+sum(nums[k:])-sum(nums[:k])
        else:
            k=n//2
            return sum(nums[k:])-sum(nums[:k])
        

