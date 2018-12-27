class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        if k==0:
            d={}
            count=0
            for i in nums:
                if i not in d:
                    d[i]=0
                elif d[i]==0:
                    count+=1
                    d[i]+=1
            return count
        vset=set(nums)
        count=0
        while vset:
            num=vset.pop()
            temp=num
            while temp+k in vset:
                temp+=k
                vset.remove(temp)
                count+=1
            temp=num
            while temp-k in vset:
                temp-=k
                vset.remove(temp)
                count+=1
        return count

nums=[1, 3, 1, 5, 4]
k = -1
c=Solution().findPairs(nums,k)