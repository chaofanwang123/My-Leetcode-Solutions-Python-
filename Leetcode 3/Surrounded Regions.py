class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            List.add((i,j))
            if i+1<m and (i+1,j) not in List and board[i+1][j]=='O':
                dfs(i+1,j)
            if i-1>=0 and (i-1,j) not in List and board[i-1][j]=='O':
                dfs(i-1,j)
            if j+1<n and (i,j+1) not in List and board[i][j+1]=='O':
                dfs(i,j+1)
            if j-1>=0 and (i,j-1) not in List and board[i][j-1]=='O':
                dfs(i,j-1)
        m=len(board)
        n=len(board[0])
        List=set([])
        for i in range(m):
            if (i,0) not in List and board[i][0]=='O':
                dfs(i,0)
            if (i,n-1) not in List and board[i][n-1]=='O':
                dfs(i,n-1)
        for j in range(n):
            if (0,j) not in List and board[0][j]=='O':
                dfs(0,j)
            if (m-1,j) not in List and board[m-1][j]=='O':
                dfs(m-1,j)
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=='O' and (i,j) not in List:
                    board[i][j]='X'

board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)

