class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=s.find(str(1-int(s[0])))
        if index==-1:
            return 0
        group=index
        i=index
        n=len(s)
        count=0
        while i<n:
            j=i+1
            while j<n and s[j]==s[j-1]:
                j+=1
            count+=min(group,j-i)
            group=j-i
            i=j
        return count
                
s="00110"
c=Solution().countBinarySubstrings(s)