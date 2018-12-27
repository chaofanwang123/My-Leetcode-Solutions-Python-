class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1=len(nums1)
        l2=len(nums2)
        if l1==0:
            if l2%2==1:
                return nums2[l2//2]
            return (nums2[l2//2]+nums2[l2//2-1])/2
        if l2==0:
            if l1%2==1:
                return nums1[l1//2]
            return (nums1[l1//2]+nums1[l1//2-1])/2
        arr=[0]*(l1+l2)
        if (l1+l2)%2==1:
            mid=(l1+l2)//2
            i=0
            j=0
            k=0
            while i<l1 and j<l2 and k<=mid:
                if nums1[i]<=nums2[j]:
                    arr[k]=nums1[i]
                    k+=1
                    i+=1
                else:
                    arr[k]=nums2[j]
                    k+=1
                    j+=1
            if k==mid+1:
                return arr[mid]
            if i==l1:
                return nums2[j+mid-k]
            return nums1[i+mid-k]
        
        if (l1+l2)%2==0:
            mid1=(l1+l2)//2
            i=0
            j=0
            k=0
            while i<l1 and j<l2 and k<=mid1:
                if nums1[i]<=nums2[j]:
                    arr[k]=nums1[i]
                    k+=1
                    i+=1
                else:
                    arr[k]=nums2[j]
                    k+=1
                    j+=1
            if k==mid1+1:
                return (arr[mid1]+arr[mid1-1])/2
            if i==l1:
                if k==mid1:
                    return (nums2[j+mid1-k]+arr[mid1-1])/2
                return (nums2[j+mid1-k]+nums2[j+mid1-1-k])/2
            
            if k==mid1:
                return (nums1[i+mid1-k]+arr[mid1-1])/2
            return (nums1[i+mid1-k]+nums1[i+mid1-1-k])/2
        
