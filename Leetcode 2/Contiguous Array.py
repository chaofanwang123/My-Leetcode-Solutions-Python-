class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d=dict()
        count0,count1=0,0
        d[0]=-1
        ans=0
        for i,num in enumerate(nums):
            if num==1:
                count1+=1
            else:
                count0+=1
            dif=count0-count1
            if dif in d:
                ans=max(ans,i-d[dif])
            else:
                d[dif]=i
        return ans

