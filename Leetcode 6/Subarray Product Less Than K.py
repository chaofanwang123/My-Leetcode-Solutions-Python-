class Solution2:
    def numSubarrayProductLessThanK2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        while i<len(nums) and nums[i]>=k:
            i+=1
        if i==len(nums):
            return 0
        nums=nums[i:]
        n=len(nums)
        mulnums=[0]*n
        mulnums[0]=nums[0]
        count=1
        startindex=[0]*n
        for i in range(1,n):
            if nums[i]>=k:
                return count+self.numSubarrayProductLessThanK2(nums[i+1:],k)
            mulnums[i]=mulnums[i-1]*nums[i]
            if mulnums[i]<k:
                startindex[i]=startindex[i-1]
                count+=i-startindex[i-1]+1
            else:
                j=startindex[i-1]
                mulnums[i]=mulnums[i]//nums[j]
                while j<i and mulnums[i]>=k:
                    j+=1
                    mulnums[i]=mulnums[i]/nums[j]
                startindex[i]=j+1
                count+=i-j
        return count
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0: return 0
        prod=1
        left=-1
        ans=0
        for right in range(len(nums)):
            prod*=nums[right]
            while prod>=k and left<right:
                left+=1
                prod//=nums[left]
            ans+=right-left
            
        return ans
                
nums = [1,2,5,3,4]
k = 5
c=Solution().numSubarrayProductLessThanK(nums,k)
