class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        pastset=set()
        end='123450'
        start=''.join([str(i) for i in board[0]+board[1]])
        if start==end:
            return 0
        cur=start.index('0')
        stack=[[start,-100,cur]]
        count=0
        d={0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[4,2]}
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                p=stack.pop(0)
                for index in d[p[2]]:
                    if index!=p[1]:
                        if index<p[2]:
                            string=p[0][:index]+p[0][p[2]]+p[0][index+1:p[2]]+p[0][index]+p[0][p[2]+1:]
                        else:
                            string=p[0][:p[2]]+p[0][index]+p[0][p[2]+1:index]+p[0][p[2]]+p[0][index+1:]
                        if string==end:
                            return count
                        if string not in pastset:
                            pastset.add(string)
                            stack.append([string,p[2],index])
        return -1
                        
board = [[1,2,3],[5,4,0]]
c=Solution().slidingPuzzle(board)                        
                    
                
            
                    
                    

