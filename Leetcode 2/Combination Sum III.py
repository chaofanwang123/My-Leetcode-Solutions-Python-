class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(target,nums,k,List):
            if k==1:
                if target in nums:
                    ans.append(List+[target])
                return
            if len(nums)>=k:
                if sum(nums[:k])<=target<=sum(nums[-k:]):
                    while len(nums)>=k:
                        dfs(target-nums[0],nums[1:],k-1,List+[nums[0]])
                        nums.pop(0)
            
        ans=[]
        nums=[1,2,3,4,5,6,7,8,9]
        if k<=0 or n<=0 or n>k*9-k*(k-1)/2:
            return []
        dfs(n,nums,k,[])
        return ans
        
c=Solution().combinationSum3(3,7)       

