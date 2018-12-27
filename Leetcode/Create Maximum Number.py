#class Solution:
#    def maxNumber(self, nums1, nums2, k):
#        """
#        :type nums1: List[int]
#        :type nums2: List[int]
#        :type k: int
#        :rtype: List[int]
#        """
#        def merge(s1,s2,maxv):
#            l1,l2=len(s1),len(s2)
#            i,j,k=0,0,0
#            while i<l1 and j<l1:
#                if int(s1[i])>
#        m,n=len(nums1),len(nums2)
#        nums1=''.join(str(item) for item in nums1)
#        nums2=''.join(str(item) for item in nums2)
#        dp1=[[0]*(m+1) for i in range(k+1)]
#        for i in range(1,min(k+1,m+1)):
#            dp1[i][i]=int(nums1[:i])
#            for j in range(i+1,m+1):
#                dp1[i][j]=max(dp1[i][j-1],dp1[i-1][j-1]*10+int(nums1[j-1]))
#        dp2=[[0]*(n+1) for i in range(k+1)]
#        for i in range(1,min(k+1,n+1)):
#            dp2[i][i]=int(nums2[:i])
#            for j in range(i+1,n+1):
#                dp2[i][j]=max(dp2[i][j-1],dp2[i-1][j-1]*10+int(nums2[j-1])) 
#        maxv=max(dp1[k][m],dp2[k][n])
#        for i in range(max(1,k-n),min(k+1,m+1)):
#            string1=str(dp1[i][m])
#            string2=str(dp2[k-i][n])
#            temp=['0']*k
#            
#            maxv=max(maxv,dp1[i][m]*pow(10,k-i)+dp2[k-i][n],dp1[i][m]+dp2[k-i][n]*pow(10,i))
#        return maxv
class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            ans = []
            L = len(nums)
            for x in range(L):
                while ans and len(ans) + L - x > t and ans[-1] < nums[x]:
                    ans.pop()
                if len(ans) < t:
                    ans += nums[x],
            return ans

        def merge(nums1, nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans
        
        m, n = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - n), min(k, m) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            res = max(tmp, res)
        return res
    
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
c=Solution().maxNumber(nums1,nums2,k)