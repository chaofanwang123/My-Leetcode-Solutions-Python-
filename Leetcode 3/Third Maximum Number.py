class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<2:
            return max(nums)
        stack=[]
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            n=len(stack)
            if n==1:
                if nums[i]>stack[0]:
                    stack+=[nums[i]]
                elif nums[i]<stack[0]:
                    stack=[nums[i]]+stack
            elif n==2:
                if nums[i]<stack[0]:
                    stack=[nums[i]]+stack
                elif stack[0]<nums[i]<stack[1]:
                    stack.insert(1,nums[i])
                if nums[i]>stack[1]:
                    stack+=[nums[i]]
            else:
                if stack[0]<nums[i]<stack[1]:
                    stack[0]=nums[i]
                elif stack[1]<nums[i]<stack[2]:
                    stack.pop(0)
                    stack.insert(1,nums[i])
                elif nums[i]>stack[2]:
                    stack.pop(0)
                    stack+=[nums[i]]
                    
        if len(stack)==3:
            return stack[0]
        return max(stack)
                    
nums=[1,3,2,2,5]
c=Solution().thirdMax(nums)
