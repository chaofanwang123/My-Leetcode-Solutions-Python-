from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=Counter(nums)
        List=sorted(d.items(),key=lambda x:-x[1])
        List2=[item[0] for item in List]
        return List2 if k>=len(List2) else List2[:k]

nums = [1,1,1,2,2,3]
k = 2
c=Solution().topKFrequent(nums,k)