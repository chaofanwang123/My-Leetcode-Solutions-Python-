class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        count0,count1=0,0
        for i in range(3):
            count0+=board[i].count('X')
            count1+=board[i].count('O')
        if count0==count1+1:
            count=0
            for i in range(3):
                if board[i]=='OOO':
                    return False
                if board[i]=='XXX':
                    count+=1
            if count>1:
                return False
            count=0
            for i in range(3):
                s=board[0][i]+board[1][i]+board[2][i]
                if s=='OOO':
                    return False
                if s=='XXX':
                    count+=1
            if count>1:
                return False
            s1=board[0][0]+board[1][1]+board[2][2]
            s2=board[2][0]+board[1][1]+board[0][2]
            return not (s1=='OOO' or s2=='OOO')
        elif count0==count1:
            count=0
            for i in range(3):
                if board[i]=='XXX':
                    return False
                if board[i]=='OOO':
                    count+=1
            if count>1:
                return False
            count=0
            for i in range(3):
                s=board[0][i]+board[1][i]+board[2][i]
                if s=='XXX':
                    return False
                if s=='OOO':
                    count+=1
            if count>1:
                return False
            s1=board[0][0]+board[1][1]+board[2][2]
            s2=board[2][0]+board[1][1]+board[0][2]
            return not (s1=='XXX' or s2=='XXX')
        return False
                    
                

