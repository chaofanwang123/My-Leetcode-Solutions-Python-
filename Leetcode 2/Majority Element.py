class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1=None
        count=0
        for i in range(len(nums)):
            if nums[i]==n1:
                count+=1
            elif count==0:
                n1=nums[i]
                count=1
            else:
                count-=1
        if n1!=None and nums.count(n1)>len(nums)//2:
            return n1
nums=[-2147483648,0,0]
c=Solution().majorityElement(nums)

