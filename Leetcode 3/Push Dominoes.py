class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n=len(dominoes)
        dominoes=list(dominoes)
        i=0
        lastindex=0
        while i<n:
            if dominoes[i]=='L':
                dominoes[lastindex:i]=['L']*(i-lastindex)
                lastindex=i+1
                i+=1
            elif dominoes[i]=='R':
                j=i+1
                while j<n and dominoes[j]=='.':
                    j+=1
                if j==n:
                    dominoes[i:]=['R']*(n-i)
                    break
                if dominoes[j]=='L':
                    if (j-i)%2:
                        mid=(i+j)//2
                        dominoes[i+1:mid+1]=['R']*(mid-i)
                        dominoes[mid+1:j]=['L']*(j-mid-1)
                        lastindex=j+1
                    else:
                        mid=(i+j)//2
                        dominoes[i+1:mid]=['R']*(mid-i-1)
                        dominoes[mid+1:j]=['L']*(j-mid-1)
                        lastindex=j+1
                    i=j+1
                else:
                    dominoes[i+1:j]=['R']*(j-i-1)
                    i=j
            else:
                i+=1
        return ''.join(dominoes)
                        
dominoes="L"
c=Solution().pushDominoes(dominoes)                
            

