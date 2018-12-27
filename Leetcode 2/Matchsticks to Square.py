class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def findindex(nums,target):
            if nums==[] or target>nums[0] or target<nums[-1]:
                return -1
            n=len(nums)
            i=0
            while i<n and target<nums[i]:
                i+=1
            if target==nums[i]:
                return i
            return -1
        def helper(nums,max_side_num,target):
            if max_side_num==1:
                idx=findindex(nums,target)
                if idx!=-1:
                    return (True,nums[:idx]+nums[idx+1:])
                return (False,nums)
            if nums[0]==target:
                return (True,nums[1:])
            if nums[-1]==target:
                return (True,nums[:-1])
            n=len(nums)
            if n==1 or n==0 or target<nums[-1]:
                return (False,nums)
            i=0
            while target<nums[i]:
                i+=1
            if i==n:
                return (False,nums)
            if target==nums[i]:
                return (True,nums[:i]+nums[i+1:])
            if target<2*nums[-1]:
                return (False,nums)
            j=i
            while j<n:
                a,b=helper(nums[i:j]+nums[j+1:],max_side_num-1,target-nums[j])
                if a:
                    return (a,nums[:i]+b) 
                j+=1
            
            if j==n:
                return (False,nums)
                
            
        n=len(nums)
        if n<4: return False
        sumall=sum(nums)
        if sumall%4!=0:
            return False
        target=sumall//4
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        
        max_side_num=n//4
        count=4
        while count>1:
            a,b=helper(nums,max_side_num,target)
            if not a:
                return False
            count-=1
            nums=b
            max_side_num=len(nums)//count
        return True
    
class Solution2:
    def makesquare(self, nums):
        def dfs(index, edge, count, used):
            for i in range(index, len(nums)):
                if i in used or edge - nums[i] < 0: continue
                elif edge - nums[i] > 0 and dfs(i + 1, edge - nums[i], count, used | {i}): return True
                elif edge - nums[i] == 0 and (count and dfs(1, l, count - 1, used | {i})) or not count: return True
            return False
        sm = sum(nums)
        if len(nums) < 4 or sm % 4 != 0: return False
        l = sm // 4 
        nums.sort(reverse = True)
        if nums[0] > l: return False
        return nums[0] == l and dfs(1, l, 1, {0}) or dfs(1, l - nums[0], 2, {0})
           
nums=[2,12,19,13,19,13,9,17,4,8,5,15,3,5,20]
c=Solution().makesquare(nums)      

