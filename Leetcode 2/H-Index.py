class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        n=len(citations)
        if citations[-1]>=n:
            return n
        for i in range(n):
            if citations[i]<i+1:
                return i