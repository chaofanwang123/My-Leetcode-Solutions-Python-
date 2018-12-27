class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A==B:
            return 0
        count=0
        k=len(A)
        i=0
        while A[i]==B[i]:
            i+=1
        pastset=set()
        stack=[[A,i]]
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                p,index=stack.pop(0)
                for j in range(index,k):
                    if p[j]==B[index]:
                        string=p[:index]+p[j]+p[index+1:j]+p[index]+p[j+1:]
                        if string==B:
                            return count    
                        if string not in pastset:
                            pastset.add(string)
                            i=index+1
                            while string[i]==B[i]:
                                i+=1
                            stack.append([string,i])
        return count


A="aaaabbbbccccddddeeee"
B="eeebcdbcdabbdeaacdca"
c=Solution().kSimilarity(A,B)