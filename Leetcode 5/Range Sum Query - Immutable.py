class NumArray:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.List=nums
        if self.List:
            n=len(nums)
            self.List=[0]*(n+1)
            for i in range(n+1):
                self.List[i]=self.List[i-1]+nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.List:
            return self.List[j+1]-self.List[i]
        
        


# Your NumArray object will be instantiated and called as such:
nums=[-4,-5]
obj = NumArray(nums)
param_1 = obj.sumRange(1,1)

