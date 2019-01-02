class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
        d={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
           11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',
           19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        s=str(num)
        List=[]
        for i in range(len(s)-1,-1,-3):
            List.insert(0,s[max(i-2,0):i+1])
        ans=''
        n=len(List)
        if n==4:
            ans+=d[int(List[0])]+' Billion '
            n-=1
            del List[0]
        if n==3:
            temp=int(List[0])
            if temp!=0:
                if temp>=100:
                    ans+=d[temp//100]+' Hundred '
                    temp%=100
                if temp>=10:
                    if temp>=20:
                        ans+=d[temp//10*10]+' '
                        temp%=10
                    else:
                        ans+=d[temp]+' '
                        temp=0
                if temp>0:
                    ans+=d[temp]+' '
                ans+='Million '
            n-=1
            del List[0]
        if n==2:
            temp=int(List[0])
            if temp!=0:
                if temp>=100:
                    ans+=d[temp//100]+' Hundred '
                    temp%=100
                if temp>=10:
                    if temp>=20:
                        ans+=d[temp//10*10]+' '
                        temp%=10
                    else:
                        ans+=d[temp]+' '
                        temp=0
                if temp>0:
                    ans+=d[temp]+' '
                ans+='Thousand '
            n-=1
            del List[0]
        temp=int(List[0])
        if temp!=0:
            if temp>=100:
                ans+=d[temp//100]+' Hundred '
                temp%=100
            if temp>=10:
                if temp>=20:
                    ans+=d[temp//10*10]+' '
                    temp%=10
                else:
                    ans+=d[temp]+' '
                    temp=0
            if temp>0:
                ans+=d[temp]+' '
        return ans[:-1] if ans[-1]==' ' else ans

num=1000010
c=Solution().numberToWords(num)
            
