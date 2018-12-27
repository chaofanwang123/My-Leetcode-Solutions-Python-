class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        d=set([])
        m=len(board)
        n=len(board[0])
        step=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    count=0
                    for u,v in step:
                        if 0<=i+u<m and 0<=j+v<n:
                            if (i+u,j+v) in d:
                                if board[i+u][j+v]==0:
                                    count+=1
                            elif board[i+u][j+v]==1:
                                count+=1
                    if count<2 or count>3:
                        board[i][j]=0
                        d.add((i,j))
                else:
                    count=0
                    for u,v in step:
                        if 0<=i+u<m and 0<=j+v<n:
                            if (i+u,j+v) in d:
                                if board[i+u][j+v]==0:
                                    count+=1
                            elif board[i+u][j+v]==1:
                                count+=1
                    if count==3:
                        board[i][j]=1
                        d.add((i,j))
            
board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
c=Solution().gameOfLife(board)                        
                        
                                
                                
                            
                            
                    

