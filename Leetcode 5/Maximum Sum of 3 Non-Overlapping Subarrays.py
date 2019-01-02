class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        sumnums=[0]*(n-k+1)
        sumnums[0]=sum(nums[:k])
        for i in range(1,n-k+1):
            sumnums[i]=sumnums[i-1]+nums[i+k-1]-nums[i-1]
        
        maxsum=sumnums[0]+sumnums[k]+sumnums[k*2]
        List=[0,k,k*2]
        maxl_index=[0]*(n-k+1)
        maxr_index=[0]*(n-k+1)
        maxr_index[-1]=n-k
        for i in range(1,n-k+1):
            if sumnums[i]>sumnums[maxl_index[i-1]]:
                maxl_index[i]=i
            else:
                maxl_index[i]=maxl_index[i-1]
        for i in range(n-k-1,-1,-1):
            if sumnums[i]>sumnums[maxr_index[i+1]]:
                maxr_index[i]=i
            else:
                maxr_index[i]=maxr_index[i+1]
        for mid in range(k,n-2*k+1):
            temp=sumnums[mid]+sumnums[maxl_index[mid-k]]+sumnums[maxr_index[mid+k]]
            if temp>maxsum:
                maxsum=temp
                List=[maxl_index[mid-k],mid,maxr_index[mid+k]]
        return List
        
nums=[1,2,1,2,6,7,5,1]
k=2
c=Solution().maxSumOfThreeSubarrays(nums,k)
