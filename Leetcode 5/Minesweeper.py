class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """             
        def dfs(i,j,m,n,d):
            #revealed[i][j]=True
            bomb=0
            stack=[]
            for a,b in d:
                x=i+a
                y=j+b
                if 0<=x<m and 0<=y<n:
                    if board[x][y]=='M':
                        bomb+=1
                    elif board[x][y]=='E':
                        stack.append([x,y])
            if stack==[]:
                board[i][j]=str(bomb) if bomb>0 else 'B'
                return
            if bomb==0:
                board[i][j]='B'
                for x,y in stack:
                    dfs(x,y,m,n,d)
            else:
                board[i][j]=str(bomb)  

        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        m=len(board)
        n=len(board[0])
        #revealed=[[False for i in range(n)] for i in range(m)]
        d=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        dfs(click[0],click[1],m,n,d)
        return board

board=[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click=[3,0]
c=Solution().updateBoard(board,click)
        

