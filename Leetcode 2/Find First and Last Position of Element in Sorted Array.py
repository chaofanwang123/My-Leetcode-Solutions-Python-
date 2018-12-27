class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                i, j = mid, mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i + 1, j - 1]
            else:
                high = mid - 1
        return [-1, -1]
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0]>target or nums[-1]<target:
            return [-1,-1]
        ans=[-1,-1]
        left=0
        right=len(nums)-1
        while left<=right and nums[left]<=target<=nums[right]:
            if nums[left]==target:
                if ans[0]==-1:
                    ans[0]=left
                else:
                    ans[0]=min(ans[0],left)
                if ans[1]==-1:
                    ans[1]=left
                else:
                    ans[1]=max(ans[1],left)
                if nums[right]==target:
                    ans[1]=max(ans[1],right)
                    return ans
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid-1
                    left+=1
                else:
                    if ans[1]==-1:
                        ans[1]=mid
                    else:
                        ans[1]=max(ans[1],mid)
                    left=mid+1
                    right-=1
            elif nums[right]==target:
                if ans[0]==-1:
                    ans[0]=right
                else:
                    ans[0]=min(ans[0],right)
                if ans[1]==-1:
                    ans[1]=right
                else:
                    ans[1]=max(ans[1],right)
                if nums[left]==target:
                    ans[0]=min(ans[0],left)
                    return ans
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                    right-=1
                else:
                    if ans[0]==-1:
                        ans[0]=mid
                    else:
                        ans[0]=min(ans[0],mid)
                    right=mid-1
                    left+=1
            else:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid-1
                    left+=1
                elif nums[mid]<target:
                    left=mid+1
                    right-=1
                else:
                    left1,right1=self.searchRange(nums[left:mid+1],target)
                    left2,right2=self.searchRange(nums[mid:right+1],target)
                    return [left1+left,right2+mid]
        if ans[0]!=-1 and ans[1]==-1:
            return [ans[0],ans[0]]
        if ans[1]!=-1 and ans[0]==-1:
            return [ans[1],ans[1]]
        return ans
nums=[0,1,2,3,3,3,4,5,5,5,6,6,7,7,8,8,9,9,11,11,12,12,12]
target=6
c=Solution().searchRange(nums,target)