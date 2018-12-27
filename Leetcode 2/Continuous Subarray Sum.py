class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        if n<2:
            return False
        if k==0:
            if nums[0]==0 and nums[1]==0:
                return True
            return False
        summ=[0]*(n+1)
        summ[1]=nums[0]
        vset=[set(),set()]
        vset[0].add(0)
        vset[1].add(0)
        vset[1].add(nums[0]%k)
        for i in range(1,n):
            summ[i+1]=summ[i]+nums[i]
            rem=summ[i+1]%k
            if i%2:
                if rem in vset[0]:
                    return True
                vset[0].add(rem)
            else:
                if rem in vset[1]:
                    return True
                vset[1].add(rem) 
        return False
        
nums=[23,2,4,6,7]
k=6
c=Solution().checkSubarraySum(nums,k)