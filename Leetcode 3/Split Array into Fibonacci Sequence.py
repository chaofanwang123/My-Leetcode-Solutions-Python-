class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def dfs(s,List):
            if not s:
                self.ans=List
                return True
            n=len(List)
            if n==0:
                for i in range(len(s)//2):
                    if i+1>1 and s[0]=='0':
                        continue
                    if int(s[:i+1])<2**31 and dfs(s[i+1:],List+[int(s[:i+1])]):
                        return True
                return False
            if n==1:
                for i in range(len(s)//2):
                    if i+1>1 and s[0]=='0':
                        continue
                    num=int(s[:i+1])
                    if int(s[:i+1])<2**31 and num+List[0]<=int(s[i+1:]) and dfs(s[i+1:],List+[int(s[:i+1])]):
                        return True
                return False
            if n>=2:
                num=List[-1]+List[-2]
                length=len(str(num))
                while s and length<=len(s) and s[:length]==str(num) and num<2**31:
                    List.append(num)
                    s=s[length:]
                    num=List[-1]+List[-2]
                    length=len(str(num))
                if not s:
                    self.ans=List
                    return True
                return False
        self.ans=[]
        dfs(S,[])
        return self.ans
                    
S="539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
c=Solution().splitIntoFibonacci(S)         
        
