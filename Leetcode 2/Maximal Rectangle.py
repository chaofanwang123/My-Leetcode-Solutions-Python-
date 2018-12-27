class Solution:       
    def maximalRectangle(self, matrix):
        def largestRectangleArea(heights):
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
    
        if matrix==[]: return 0
        a=[0 for i in range(len(matrix[0]))]; maxArea=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j]=a[j]+1 if matrix[i][j]=='1' else 0
            maxArea=max(maxArea, largestRectangleArea(a))
        return maxArea

matrix=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
c=Solution().maximalRectangle(matrix)