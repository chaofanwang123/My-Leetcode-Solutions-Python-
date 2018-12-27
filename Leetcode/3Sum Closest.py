class Solution:
    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minvalue=float('inf')
        sumvalue=0
        n=len(nums)
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                sumv=nums[i]+nums[left]+nums[right]
                diff=abs(sumv-target)
                if diff<minvalue:
                    minvalue=diff
                    sumvalue=sumv
                if diff==0:
                    return sumv
                elif sum<target:
                    left+=1
                else:
                    right-=1
            return sumvalue
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twosumcloset(nums,target2):
            nums2=[target2-i for i in nums]
            for i in range(n-1):
                temp=nums[i]
                del nums[i]
                s1,s2=0,n-3
                while s1<=s2 and nums2[i]+self.minv>nums[s1] and nums2[i]-self.minv<nums[s2]:
                    if nums2[i]==nums[s1] or nums2[i]==nums[s2]:
                        return True
                    mid=(s1+s2)//2
                    if nums[mid]==nums2[i]:
                        return True
                    if nums[mid]>nums2[i]:
                        s2=mid-1
                    else:
                        s1=mid+1
                if s1>s2:
                    if s1<n-2 and abs(nums[s1]-nums2[i])<self.minv:
                        self.minv=abs(nums[s1]-nums2[i])
                        self.sumvalue=nums[s1]-nums2[i]+target
                    if abs(nums[s2]-nums2[i])<self.minv:
                        self.minv=abs(nums[s2]-nums2[i])
                        self.sumvalue=nums[s2]-nums2[i]+target
                nums.insert(i,temp)
            return False
            
        nums.sort()
        n=len(nums)
        if n==3:
            return sum(nums)
        if sum(nums[:3])>=target:
            return sum(nums[:3])
        if sum(nums[-3:])<=target:
            return sum(nums[-3:])
        i=0
        while sum(nums[i:i+3])<target:
            i+=1
        if sum(nums[i:i+3])==target:
            return target
        a=sum(nums[i-1:i+2])
        b=sum(nums[i:i+3])
        self.minv=abs(a-target)
        self.sumvalue=a
        if abs(b-target)<self.minv:
            self.minv=abs(b-target)
            self.sumvalue=b
            
        for i in range(n):
            if twosumcloset(nums[:i]+nums[i+1:],target-nums[i]):
                return target
        return self.sumvalue
            
nums=[0,2,1,-3]
c=Solution().threeSumClosest(nums,1)

