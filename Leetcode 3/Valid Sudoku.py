class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            d1=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in d1:
                        return False
                    d1.add(board[i][j])
        for j in range(9):
            d1=set()
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in d1:
                        return False
                    d1.add(board[i][j])
        for i in range(3):
            for j in range(3):
                d1=set()
                for k in range(3*i,3*(i+1)):
                    for r in range(3*j,3*(j+1)):
                        if board[k][r]!='.':
                            if board[k][r] in d1:
                                return False
                            d1.add(board[k][r])
        return True
            

