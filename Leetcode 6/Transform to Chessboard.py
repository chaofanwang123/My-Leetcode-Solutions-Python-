class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n=len(board)
        if n%2:
            sumi=sum(board[0])
            d=n//2
            if sumi!=d and sumi!=n-d:
                return -1
            sumj=0
            for i in range(n):
                sumj+=board[i][0]
            if sumj!=d and sumj!=n-d:
                return -1
            
            h1=board[0]
            h2=[1-board[0][j] for j in range(n)]
            count_h1,count_h2=1,0
            v1=[board[i][0] for i in range(n)]
            v2=[1-board[i][0] for i in range(n)]
            count_v1,count_v2=1,0
            
            for i in range(1,n):
                if board[i]==h1:
                    count_h1+=1
                elif board[i]==h2:
                    count_h2+=1
                else:
                    return -1
                temp=[board[j][i] for j in range(n)]
                if temp==v1:
                    count_v1+=1
                elif temp==v2:
                    count_v2+=1
                else:
                    return -1
                if abs(count_h1-count_h2)>n-i or abs(count_v1-count_v2)>n-i:
                    return -1
            
            swap_h,swap_v=0,0
            for i in range(d):
                if h1[2*i]!=0:
                    swap_h+=1
                if h1[2*i+1]!=1:
                    swap_h+=1
                if v1[2*i]!=0:
                    swap_v+=1
                if v1[2*i+1]!=1:
                    swap_v+=1
            if h1[-1]!=0:
                swap_h+=1
            if v1[-1]!=0:
                swap_v+=1
            if swap_h%2:
                if swap_v%2:
                    return (n-swap_h)//2+(n-swap_v)//2
                else:
                    return (n-swap_h)//2+swap_v//2
            else:
                if swap_v%2:
                    return swap_h//2+(n-swap_v)//2
                else:
                    return swap_h//2+swap_v//2
        else:
            d=n//2
            if sum(board[0])!=d:
                return -1
            sumj=0
            for i in range(n):
                sumj+=board[i][0]
            if sumj!=d:
                return -1
            
            h1=board[0]
            h2=[1-board[0][j] for j in range(n)]
            count_h1,count_h2=1,0
            v1=[board[i][0] for i in range(n)]
            v2=[1-board[i][0] for i in range(n)]
            count_v1,count_v2=1,0
            
            for i in range(1,n):
                if board[i]==h1:
                    count_h1+=1
                elif board[i]==h2:
                    count_h2+=1
                else:
                    return -1
                temp=[board[j][i] for j in range(n)]
                if temp==v1:
                    count_v1+=1
                elif temp==v2:
                    count_v2+=1
                else:
                    return -1
                if abs(count_h1-count_h2)>n-i-1 or abs(count_v1-count_v2)>n-i-1:
                    return -1
            
            swap_h,swap_v=0,0
            for i in range(d):
                if h1[2*i]!=0:
                    swap_h+=1
                if h1[2*i+1]!=1:
                    swap_h+=1
                if v1[2*i]!=0:
                    swap_v+=1
                if v1[2*i+1]!=1:
                    swap_v+=1
            return min(swap_h,n-swap_h)//2+min(swap_v,n-swap_v)//2
            
board=[[0,1,1,0,1],[0,1,1,0,1],[1,0,0,1,0],[1,0,0,1,0],[0,1,1,0,1]]
c=Solution().movesToChessboard(board)                
