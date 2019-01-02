from collections import defaultdict
class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A==B:
            return 0
        d1=defaultdict(set)
        d2=defaultdict(set)
        k=len(A)
        for i in range(k):
            d1[A[i]].add(i)
            d2[B[i]].add(i)
        ListA=sorted(d1.items())
        ListB=sorted(d2.items())
        i=len(ListA)-1
        while i>=0:
            if ListA[i][1]==ListB[i][1]:
                del ListA[i]
                del ListB[i]
            i-=1       
        dic1,dic2={},{}
        for i in range(len(ListA)):
            swapA=ListA[i][1]-ListB[i][1]
            swapB=ListB[i][1]-ListA[i][1]
            dic1[ListA[i][0]],dic2[ListA[i][0]]=swapA,swapB
        count=0
        for x in dic1.keys():
            temp=[]
            while dic1[x]:
                note=0
                index=dic1[x].pop()
                for index2 in dic1[B[index]]:
                    if index2 in dic2[x]:
                        dic1[B[index]].remove(index2)
                        dic2[x].remove(index2)
                        #dic1[x].remove(index)
                        dic2[B[index]].remove(index)
                        note=1
                        count+=1
                        break
                if note==0:
                    temp.append(index)
            if temp:
                while dic2[x]:
                    count+=1
                    index=temp.pop()
                    index2=dic2[x].pop()
                    dic1[A[index2]].remove(index2)
                    dic1[A[index2]].add(index)
                    tempA=list(A)
                    tempA[index],tempA[index2]=tempA[index2],tempA[index]
                    A=''.join(tempA)
        return count
                        
#            while dic1[x]:
#                note=0
#                for index in dic1[x]:
#                    for index2 in dic1[B[index]]:
#                        if index2 in dic2[x]:
#                            dic1[B[index]].remove(index2)
#                            dic2[x].remove(index2)
#                            dic1[x].remove(index)
#                            dic2[B[index]].remove(index)
                
        
            
        
                                
class Solution2:
    def kSimilarity2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A==B:
            return 0
        pastset=set()
        pastset.add(A)
        stack=[A]
        count=0
        k=len(A)
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                p=stack.pop(0)
                for i in range(k-1):
                    for j in range(i+1,k):
                        if p[i]!=p[j]:
                            string=p[:i]+p[j]+p[i+1:j]+p[i]+p[j+1:]
                            if string==B:
                                return count
                            if string not in pastset:
                                pastset.add(string)
                                stack.append(string)

A="abccaacceecdeea"
B="bcaacceeccdeaae"
c=Solution().kSimilarity(A,B)
        
                

