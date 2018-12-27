class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(array,target):
            left=0
            right=len(array)-1
            if target>2*array[-1] or target<2*array[0]:
                return []
            ans1=[]
            while left<right:
                summ=array[left]+array[right]
                if summ==target:
                    ans1.append([array[left],array[right]])
                    left+=1
                    right-=1
                elif summ<target:
                    left+=1
                else:
                    right-=1
            return ans1
                    
        n=len(nums)
        if n<3:
            return []
        nums.sort()
        i=n-1
        note=0
        while i>=2:
            if nums[i-2]==nums[i]:
                if nums[i]==0:
                    note=1
                del nums[i]
            i-=1
        ans=set([])
        if note==1:
            ans.add((0,0,0))
        n=len(nums)
        if n<3:
             return [list(item) for item in ans]
        
        for i in range(n-2):
            for item in helper(nums[i+1:],-nums[i]):
                ans.add(tuple([nums[i]]+item))
        return [list(item) for item in ans]

nums = [-1, 0, 1, 2, -1, -4]
c=Solution().threeSum(nums)