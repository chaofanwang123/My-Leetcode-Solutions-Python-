from collections import defaultdict
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d=defaultdict(list)
        n=len(nums)
        ans=set()
        for i in range(n-1):
            for j in range(i+1,n):
                d[nums[i]+nums[j]].append([i,j])
        for item in d:
            if target-item in d:
                for u,v in d[item]:
                    for x,y in d[target-item]:
                        if u!=x and u!=y and v!=x and v!=y:
                            temp=sorted([nums[u],nums[v],nums[x],nums[y]])
                            ans.add(tuple(temp))
        return [list(item) for item in list(ans)]
                
nums = [1, 0, -1, 0, -2, 2]
target = 0
c=Solution().fourSum(nums,target)        

