class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        n=len(S)
        i=0
        List=[]
        while i<n-1:
            if S[i]==S[i+1]:
                start=i
                i+=1
                while i<n-1 and S[i]==S[i+1]:
                    i+=1
                if i-start>=2:
                    List.append([start,i])
            i+=1
        return List
