class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n=len(board)
        if n%2:
            count=0
            d1={n//2:0,(n+1)//2:0}
            d2={n//2:0,(n+1)//2:0}
            for i in range(n):
                sumi=sum(board[i])
                if sumi not in d1:
                    return -1
                d1[sumi]+=1
                sumj=0
                for j in range(n):
                    sumj+=board[j][i]
                if sumj not in d2:
                    return -1
                d2[sumj]+=1
                if i%2:
                    if sumi!=(n+1)//2:
                        count+=1
                    if sumj!=(n+1)//2:
                        count+=1
                else:
                    if sumi!=n//2:
                        count+=1
                    if sumj!=n//2:
                        count+=1
            if d1[n//2]==d2[n//2] and d1[(n+1)//2]==d2[(n+1)//2]:
                if d1[n//2]==n//2 and d1[(n+1)//2]==(n+1)//2:
                    return n-count//2
                elif d1[n//2]==(n+1)//2 and d1[(n+1)//2]==n//2:
                    return count//2
                return -1
            return -1
        else:
            d=n//2
            count1,count2=0,0
            if sum(board[0])!=d:
                return -1
            sumj=0
            for j in range(n):
                sumj+=board[j][0]
            if sumj!=d:
                return -1
            for i in range(d):
                if board[0][2*i]!=0:
                    count1+=1
                if board[0][2*i+1]!=1:
                    count1+=1
                if board[2*i][0]!=0:
                    count2+=1
                if board[2*i+1][0]!=1:
                    count2+=1

            for i in range(1,n):
                for j in range(d):
                    if board[i][j]
            
            return min(count,2*n-count)//2
            
board = [[0,0,1,1],[1,1,0,0],[0,1,0,1],[1,0,1,0]]
c=Solution().movesToChessboard(board)
            

