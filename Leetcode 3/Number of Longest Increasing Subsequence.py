import bisect
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=0:
            return n
        List=[nums[0]]
        d={nums[0]:1}
        for num in nums[1:]:
            if  num>List[-1]:
                List.append(num)
                count=0
                for item in d:
                    if item<num:
                        count+=d[item]
                d={num:count}
            elif num==List[-1]:
                d[num]+=d[num]
            else:
                index=bisect.bisect_left(List,num)
                if index==len(List)-1:
                    d[num]=1
                List[index]=num
        return sum(d.values())
        
nums=[1,1,1,2,2,2,3,3,3]
c=Solution().findNumberOfLIS(nums)