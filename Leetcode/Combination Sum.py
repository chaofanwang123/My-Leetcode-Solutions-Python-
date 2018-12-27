class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(nums,target):
            if target<0:
                return []
            if target==0:
                return [[]]
            j=len(nums)-1
            ans=[]
            if nums[0]>target:
                return ans
            while nums[j]>target:
                del nums[j]
                j-=1
            if nums[j]==target:
                ans.append([nums[j]])
                del nums[j]
        
            for i in range(len(nums)):
                if nums[i]<=target:
                    temp=helper(nums[i:],target-nums[i])
                    for item in temp:
                        ans.append([nums[i]]+item)
            return ans
            
        candidates.sort()
        return helper(candidates,target)

candidates=[2,3,5]
target=8
c=Solution().combinationSum(candidates,target)