from collections import Counter
import math
class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        d=Counter(answers)
        ans=0
        for item in d:
            ans+=math.ceil(d[item]/(item+1))*(item+1)
        return ans
        

