class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        n=len(heights)
        if n==1:
            return heights[0]
        maxarea=0
        stackheight,stackindex=[],[]
        n=len(heights)
        for i in range(n):
            if stackheight==[] or heights[i]>stackheight[-1]:
                stackheight.append(heights[i])
                stackindex.append(i)
            else:
                index=0
                while stackheight!=[] and heights[i]<=stackheight[-1]:
                    h,index=stackheight.pop(),stackindex.pop()
                    maxarea=max(maxarea,h*(i-index))
                stackheight.append(heights[i])
                stackindex.append(index)
        while stackheight:
            h,index=stackheight.pop(),stackindex.pop()
            maxarea=max(maxarea,h*(n-index))
        return maxarea
heights=[]
c=Solution().largestRectangleArea(heights)

