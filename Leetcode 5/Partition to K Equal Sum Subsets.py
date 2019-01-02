import bisect
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(k,visited,target):
            if k==1:
                return True
            if target==0:
                if dfs(k-1,visited,avg):
                    return True
            index=bisect.bisect_right(nums,target)
            for i in range(index-1,-1,-1):
                if not visited[i]:
                    visited[i]=True
                    if dfs(k,visited,target-nums[i]):
                        return True
                    visited[i]=False
            return False
        if k==1:
            return True
        nums.sort()
        total=sum(nums)
        if total%k!=0 or total//k<nums[-1]:
            return False
        avg=total//k
        n=len(nums)
        visited=[False]*n
        visited[-1]=True
        return dfs(k,visited,avg-nums[-1])

nums =[5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3]
k=15
c=Solution().canPartitionKSubsets(nums,k)