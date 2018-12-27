from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words:
            return []
        d=Counter(words)
        List=sorted(d.items(),key=lambda x:(-x[1],x[0]))
        if k>=len(List):
            return [item[0] for item in List]
        else:
            return [item[0] for item in List[:k]]
