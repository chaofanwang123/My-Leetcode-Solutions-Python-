class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        n=len(start)
        i=0
        while i<n:
            if start[i]=='R':
                index=end.find('L',i)
                if index==-1:
                    index=n
                if index==i or start[i:index].count('R')!=end[i:index].count('R'):
                    return False
                i=index
            elif start[i]=='L':
                if end[i]!='L':
                    return False
                i+=1
            else:
                if end[i]=='R':
                    return False
                if end[i]=='L':
                    index=start.find('R',i)
                    if index==-1:
                        index=n
                    if index==i or start[i:index].count('L')!=end[i:index].count('L'):
                        return False
                    i=index
                else:
                    i+=1
        return True
                
start="RL"
end="LR"  
c=Solution().canTransform(start,end)             
            
