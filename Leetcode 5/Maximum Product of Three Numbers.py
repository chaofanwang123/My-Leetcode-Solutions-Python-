class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==3:
            return nums[0]*nums[1]*nums[2]
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
class Solution2(object):
    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = pa = pb = pc = None
        na = nb = float('inf')
        for n in nums:
            if n > pa: pa, pb, pc = n, pa, pb
            elif n > pb: pb, pc = n, pb
            elif n > pc: pc = n
            if n < na: na, nb = n, na
            elif n < nb: nb = n
        return max(ans, pa * na * nb, pa * pb * pc)
