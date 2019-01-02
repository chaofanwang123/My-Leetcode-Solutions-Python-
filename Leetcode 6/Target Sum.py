class Solution2:
    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def allsum(nums,target):
            n=len(nums)
            d={0:1}
            i=0
            while i<n and nums[i]<=target:
                d2={}
                for item in d:
                    temp=nums[i]+item
                    if temp<=target:
                        if temp not in d2:
                            d2[temp]=1
                        else:
                            d2[temp]+=1
                for item in d2:
                    if item in d:
                        d[item]+=d2[item]
                    else:
                        d[item]=d2[item]
                i+=1
            return d
        summ=sum(nums)
        if S<-summ or S>summ or (summ-S)%2==1:
            return 0
        target=(summ-S)//2
        n=len(nums)
        if n==1:
            count=0
            if nums[0]==target:
                count+=1
            if nums[0]==-target:
                count+=1
            return count
        d1=allsum(nums[:n//2],target)
        d2=allsum(nums[n//2:],target)
        count=0
        for item in d2:
            if target-item in d1:
               count+=d1[target-item]*d2[item] 
        return count

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums.sort()
        summ=sum(nums)
        if S<-summ or S>summ or (summ-S)%2==1:
            return 0
        target=(summ-S)//2
        n=len(nums)
        dp=[0]
        i=0
        count=1 if target==0 else 0
        while i<n and nums[i]<=target:
            dp0=[]
            for item in dp:
                temp=nums[i]+item
                if temp<=target:
                    dp0.append(temp)
                    if temp==target:
                        count+=1
            dp+=dp0
            i+=1
        return count
    
class Solution3:
    def findTargetSumWays3(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        c = [0]*1001
        c[0] = 1
        T = sum(nums)
        A = T+S
        if T<S or A&1:
            return 0
        A>>=1
        nums = sorted(nums)
        temp = 0
        for ind, v in enumerate(nums):
            temp += v
            for i in range(min(temp, A), v-1, -1):
                c[i] += c[i-v]
        return c[A]
nums=[14,23,35,48,10,39,34,40,36,45,11,14,41,6,4,17,42,22,0,35]
S=44
#nums=[1,1,1,1,1]
#S=3
c=Solution3().findTargetSumWays3(nums,S)