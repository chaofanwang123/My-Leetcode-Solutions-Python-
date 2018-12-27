class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return slow

nums=[3,4,1,2,3]
c=Solution().findDuplicate(nums)

