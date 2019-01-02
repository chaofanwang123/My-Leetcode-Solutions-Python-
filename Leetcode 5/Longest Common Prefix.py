class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        ans=''
        minl=len(strs[0])
        for i in strs:
            minl=min(minl,len(i))
        for j in range(minl):
            letter=strs[0][j]
            for i in strs:
                if i[j]!=letter:
                    return ans
            ans+=letter
        return ans

