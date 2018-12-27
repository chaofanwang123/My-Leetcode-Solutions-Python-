class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0 or n==1:
            return n
        start=0
        end=0
        d=dict()
        max_length=1
        while end<n:
            if s[end] not in d:
                d[s[end]]=end
            else:
                if start<=d[s[end]]<end:
                    if end-start>max_length:
                        max_length=end-start
                    start=d[s[end]]+1
                d[s[end]]=end
            end+=1
        if n-start>max_length:
            max_length=end-start
        return max_length
