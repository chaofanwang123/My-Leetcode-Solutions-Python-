class Solution:
    def canJump(self, nums):
        n=len(nums)
        if n==1 or nums[0]>=n-1:
            return True
        index1=0
        index2=nums[0]
        while True:
            if index1==index2:
                return False
            maxv=index1+1+nums[index1+1]
            if maxv>=n-1:
                return True
            for i in range(index1+2,index2+1):
                maxv=max(maxv,i+nums[i])
                if maxv>=n-1:
                    return True
            index1,index2=index2,maxv
                

nums=[2,3,1,1,4]
c=Solution().canJump(nums)

