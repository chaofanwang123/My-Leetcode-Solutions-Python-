class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        
        count=len(nums1)-m
        while count>0:
            nums1.pop()
            count-=1
        while i<m and j<n:
            if nums1[i]>nums2[j]:
                nums1.insert(i,nums2[j])
                i+=1
                m+=1
                j+=1
            else:
                i+=1
        if i==m:
            if j!=n:
                nums1+=nums2[j:]
        
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
c=Solution().merge(nums1,m,nums2,n)
