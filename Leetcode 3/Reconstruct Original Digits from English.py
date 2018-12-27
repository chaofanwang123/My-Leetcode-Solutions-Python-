from collections import Counter
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[0]*10
        List=[['z','zero',0],['u','four',4],['f','five',5],['v','seven',7],['x','six',6],['w','two',2],
              ['r','three',3],['t','right',8],['i','nine',9],['o','one',1]]
        d=Counter(s)
        if not d:
            return ''
        for letter,words,index in List:
            if letter in d:
                arr[index]=d[letter]
                for word in words:
                    d[word]-=arr[index]
                    if d[word]==0:
                        del d[word]
                if not d:
                    break
        ans=''
        for i in range(10):
            if arr[i]!=0:
                ans+=str(i)*arr[i]
        return ans
                
s="fviefuro"
c=Solution().originalDigits(s)