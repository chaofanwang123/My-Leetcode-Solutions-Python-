import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        A=sorted(envelopes, key=lambda x:(x[0],-x[1]))
        nums=[item[1] for item in A]
        stack=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>stack[-1]:
                stack.append(nums[i])
            elif nums[i]<stack[-1]:
                stack[bisect.bisect_left(stack,nums[i])]=nums[i]
        return len(stack)

envelopes=[[5,4],[5,3],[6,4],[6,7],[2,3],[2,4],[2,5]]
c=Solution().maxEnvelopes(envelopes)