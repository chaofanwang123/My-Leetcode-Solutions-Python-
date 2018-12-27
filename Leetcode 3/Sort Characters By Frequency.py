from collections import Counter
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        d=Counter(list(s))
        List=sorted(d.items(),key=lambda x:-x[1])
        ans=''
        for key, count in List:
            ans+=key*count
        return ans
        
