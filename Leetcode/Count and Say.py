class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string='1'
        for i in range(1,n):
            j=0
            temp=''
            while j<len(string):
                k=j
                while k<len(string)-1 and string[k]==string[k+1]:
                    k+=1
                temp+=str(k-j+1)+string[j]
                j=k+1
            string=temp
        return string
                

