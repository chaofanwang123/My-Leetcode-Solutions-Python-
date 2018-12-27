class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Nums=set(nums)
        length=0
        while Nums:
            i=Nums.pop()
            count=1
            j=i+1
            while j in Nums:
                Nums.remove(j)
                j+=1
                count+=1
            j=i-1
            while j in Nums:
                Nums.remove(j)
                j-=1
                count+=1
            length=max(length,count)
        return length

nums=[100, 4, 200, 1, 3, 2]
c=Solution().longestConsecutive(nums)
            

