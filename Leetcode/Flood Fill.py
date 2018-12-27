class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(i,j):
            image[i][j]=newColor
            if i+1<m and image[i+1][j]==oldcolor:
                dfs(i+1,j)
            if i-1>=0 and image[i-1][j]==oldcolor:
                dfs(i-1,j)
            if j+1<n and image[i][j+1]==oldcolor:
                dfs(i,j+1)
            if j-1>=0 and image[i][j-1]==oldcolor:
                dfs(i,j-1)
        m=len(image)
        n=len(image[0])
        oldcolor=image[sr][sc]
        if oldcolor!=newColor:
            dfs(sr,sc)
        return image

image=[[0,0,0],[0,1,1]]
sr=1
sc=1
newColor=1
c=Solution().floodFill(image,sr,sc,newColor)