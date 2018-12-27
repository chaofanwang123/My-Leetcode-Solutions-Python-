class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d=set([])
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return True
        return False

