from collections import defaultdict
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
#        def dfs(i,j,matrix,m,n,vlist,list2,value,truelist):
#            if [i,j]==[0,0]:
#                truelist[0]=True
#                if truelist[1]:
#                    return truelist
#                vlist[i][j]=True
#                if i+1<m and matrix[i+1][j]<=value:
#                    if list2[i+1][j]=
                    
# =============================================================================
#                 
#                 
#             if [i,j]==[m-1,n-1]:
#                 truelist
#             
#             vlist[i][j]=True
#             if i+1<m and matrix[i+1][j]<=value:
#                 dfs(i+1,j,matrix,m,n,vlist,value)
#             if i-1>=0 and [i-1,j]!=pastindex and vlist[i-1][j]==False and matrix[i-1][j]>=maxv:
#                 dfs(i-1,j,matrix,m,n,vlist,[i,j],maxv)
#             if j+1<n and [i,j+1]!=pastindex and vlist[i][j+1]==False and matrix[i][j+1]>=maxv:
#                 dfs(i,j+1,matrix,m,n,vlist,[i,j],maxv)
#             if j-1>=0 and [i,j-1]!=pastindex and vlist[i][j-1]==False and matrix[i][j-1]>=maxv:
#                 dfs(i,j-1,matrix,m,n,vlist,[i,j],maxv)
#             vlist[i][j]=True
# =============================================================================
        def cut(cutlist,m,n):
            
        if matrix==[]:
            return []
        m=len(matrix)
        n=len(matrix[0])
        vlist=[[False for i in range(n)] for j in range(m)]
        List=[]
        for i in range(m):
            for j in range(n):
                List.append((matrix[i][j],[i,j]))
        List.sort(reverse=True)
        maxv=max(matrix[0][0],matrix[m-1][n-1])
        cutlist=[]
        finalist=[]
        for value,index in List:
            if value<maxv or cut(cutlist,m,n):
                break
            finallist.append(index)
            cutlist.append(index)
            

    
matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
c=Solution().pacificAtlantic(matrix)
            
            
