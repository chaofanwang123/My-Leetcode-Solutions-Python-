class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dp=['']
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        for string in digits:
            temp=[]
            for x in d[string]:
                temp+=[item+x for item in dp]
            dp=temp
        return dp
            
digits='23'
c=Solution().letterCombinations(digits)
