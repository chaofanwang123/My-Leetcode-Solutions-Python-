class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i=0
        n=len(words)
        ans=[]
        while i<n:
            length=len(words[i])
            List=[words[i]]
            j=i+1
            while j<n and length+len(words[j])+1<=maxWidth:
                length+=len(words[j])+1
                List.append(' '+words[j])
                j+=1
            if j<n:
                remlength=maxWidth-length
                m=len(List)
                if m==1:
                    List[0]+=' '*remlength
                    ans.append(''.join(List))
                else:
                    k,rem=remlength//(m-1),remlength%(m-1)
                    for l in range(rem):
                        List[l]+=' '*(k+1)
                    for l in range(rem,m-1):
                        List[l]+=' '*k
                    ans.append(''.join(List))
            else:
                s=''.join(List)
                ans.append(s+' '*(maxWidth-len(s)))
            i=j
        return ans
                        
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
c=Solution().fullJustify(words,maxWidth)                
                
            
            

