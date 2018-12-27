class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(List,value):
            s
        n=len(boxes)
        i=0
        List=[]
        while i<n:
            j=i+1
            while j<n and boxes[j]==boxes[j-1]:
                j+=1
            List.append([boxes[j-1],j-i])    
            i=j
        dp=[1]
        m=len(List)
        maxv=0
        for k in range(m):
            for i in range(k):
                if List[i][0]==List[k][0]:
                    dp[i][0]+dp[i+1][1]+(List[i][1]+List[k][1])**2
                    
        

