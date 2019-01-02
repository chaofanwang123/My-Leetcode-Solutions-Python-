class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i,j,word):
            if word=='':
                return True
            visited[i][j]=True
            if i+1<m and not visited[i+1][j] and board[i+1][j]==word[0]:
                if dfs(i+1,j,word[1:]):
                    return True
            if i-1>=0 and not visited[i-1][j] and board[i-1][j]==word[0]:
                if dfs(i-1,j,word[1:]):
                    return True
            if j+1<n and not visited[i][j+1] and board[i][j+1]==word[0]:
                if dfs(i,j+1,word[1:]):
                    return True
            if j-1>=0 and not visited[i][j-1] and board[i][j-1]==word[0]:
                if dfs(i,j-1,word[1:]):
                    return True
            visited[i][j]=False
            
        if word=='' or board==[] or board==[[]]:
            return False
        m=len(board)
        n=len(board[0])
        visited=[[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and dfs(i,j,word[1:]):
                    return True
        return False
board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"
c=Solution().exist(board,word)
        

