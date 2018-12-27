class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n=len(nums)
        if n==0:
            return []
        List=[[]]
        for i in range(n):
            temp=[]
            for j in range(i+1):
                for item in List:
                    item2=item[:j]+[nums[i]]+item[j:]
                    if item2 not in temp:
                        temp.append(item2)
            List=temp
        return List

nums=[1,1,2]
c=Solution().permuteUnique(nums)


