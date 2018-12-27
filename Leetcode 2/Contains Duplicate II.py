from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        if n<2:
            return False
        d=defaultdict(list)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                if i-d[nums[i]][-1]<=k:
                    return True
                d[nums[i]].append(i)
        return False
            
nums=[99,99]
c=Solution().containsNearbyDuplicate(nums,2)