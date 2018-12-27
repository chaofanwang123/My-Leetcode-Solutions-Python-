class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>=n-1:
            return 1
        count=1
        index1=0
        index2=nums[0]
        while True:
            count+=1
            maxv=index1+1+nums[index1+1]
            if maxv>=n-1:
                return count
            for i in range(index1+2,index2+1):
                maxv=max(maxv,i+nums[i])
                if maxv>=n-1:
                    return count
            index1,index2=index2,maxv
                

nums=[0]
c=Solution().jump(nums)