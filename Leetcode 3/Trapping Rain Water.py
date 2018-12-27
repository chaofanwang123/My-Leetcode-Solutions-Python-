class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n<=1:
            return 0
        i=0
        stack=[]
        area1=0
        area2=0
        while i<n:
            if not stack or height[i]<=height[stack[-1]]:
                stack.append(i)
            else:
                temparea=0
                while stack and height[stack[-1]]<=height[i]:
                    index=stack.pop()
                    temparea+=height[index]
                if not stack:
                    area2+=height[index]*(i-index)-temparea
                else:
                    area1+=temparea
                stack.append(i)
            i+=1
        for i in range(len(stack)-1,0,-1):
            area2+=height[stack[i]]*(stack[i]-stack[i-1]-1)
        return area2-area1

class Solution2:
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

height=[0,1,0,2,1,0,1,3,2,1,2,1]
c=Solution2().trap2(height)