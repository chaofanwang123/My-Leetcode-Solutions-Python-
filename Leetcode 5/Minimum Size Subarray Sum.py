class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def binarysearch(nums):
            m=len(nums)
            if m==1:
                return 1
            left=0
            right=m-1
            if nums[-1]-nums[0]<s:
                return n
            while left<right:
                mid=(left+right)//2
                if nums[-1]-nums[mid]==s:
                    return m-1-mid
                if nums[-1]-nums[mid]>s:
                    left=mid+1
                else:
                    right=mid-1
            if nums[-1]-nums[left]<s:
                return m-left
            else:
                return m-1-left
            
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return 1 if nums[0]>=s else 0
        if nums[0]>=s:
            return 1
        for i in range(1,n):
            if nums[i]>=s:
                return 1
            nums[i]+=nums[i-1]
        if nums[-1]<s:
            return 0
        left=0
        right=n-1
        index=-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==s:
                index=mid 
                break
            if nums[mid]<s:
                left=mid+1
            else:
                right=mid-1
        if index==-1:
            if nums[left]<s:
                index=left+1
            else:
                index=left
        length=index+1
        for i in range(index,n):
            length=min(length,binarysearch(nums[i+1-length:i+1]))
        return length
            
#        nums=[0]+nums
#        left=0
#        right=n
#        length=right-left
#        while left<right and nums[right]-nums[left]>=s:
#            length=right-left
#            a=nums[left+1]-nums[left]
#            b=nums[right]-nums[right-1]
#            if a>b:
#                right-=1
#            else:
#                left+=1
        
s = 11
nums = [1,2,3,4,5]        
c=Solution().minSubArrayLen(s,nums)        

