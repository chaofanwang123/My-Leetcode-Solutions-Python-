class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            i=0
            j=len(nums)-1
            while i<=j and nums[i]==0:
                i+=1
            if i==j:
                return
            while j>i and nums[j]==2:
                j-=1
            if j==i:
                return
            k=i
            while k<j+1:
                if nums[k]==0:
                    del nums[k]
                    nums.insert(0,0)
                    k+=1
                elif nums[k]==2:
                    del nums[k]
                    nums.append(2)
                    j-=1
                else:
                    k+=1
class Solution2:
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[i] = 1
                i += 1
            if v == 0:
                nums[j] = 0
                j += 1
nums=[2,0,2,1,1,0]
Solution2().sortColors2(nums)
                    
            

