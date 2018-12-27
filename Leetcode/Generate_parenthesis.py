class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        List=[[]]*n
        List[0]=['()']
        for m in range(1,n):
            for i in range(m):
                List[m]=List[m]+[item1+item2 for item1 in List[i] for item2 in List[m-1-i]]
            List[m]=List[m]+['('+item3+')' for item3 in List[m-1]]
        return list(set(List[n-1]))

c=Solution().generateParenthesis(3)