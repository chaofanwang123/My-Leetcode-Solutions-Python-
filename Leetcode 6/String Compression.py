class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=len(chars)-1
        while i>=0:
            j=i-1
            while j>=0 and chars[j]==chars[j+1]:
                j-=1
            length=i-j
            if length>1:
                chars[j+2:i+1]=[]
                word=str(length)
                for m in range(len(word)):
                    chars.insert(j+2+m,word[m])
            i=j
        return len(chars)

chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
c=Solution().compress(chars)