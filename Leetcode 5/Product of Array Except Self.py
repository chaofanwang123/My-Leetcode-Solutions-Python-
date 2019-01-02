class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        index=-1
        mul1=1
        for i in range(n):
            if nums[i]==0:
                if index!=-1:
                    return [0]*n
                index=i
            else:
                mul1=mul1*nums[i]
        if index==-1:
            return [mul1//item for item in nums]
        nums=[0]*n
        nums[index]=mul1
        return nums

