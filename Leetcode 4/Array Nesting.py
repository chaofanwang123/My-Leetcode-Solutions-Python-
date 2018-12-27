class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        vset=set()
        maxcount=0
        for i in range(n):
            if nums[i] not in vset:
                temp=nums[i]
                vset.add(nums[i])
                count=1
                while nums[temp] not in vset:
                    vset.add(nums[temp])
                    temp=nums[temp]
                    count+=1
                maxcount=max(maxcount,count)
        return maxcount
 
nums=[1,0,3,4,2]
c=Solution().arrayNesting(nums)           
            
                
        

