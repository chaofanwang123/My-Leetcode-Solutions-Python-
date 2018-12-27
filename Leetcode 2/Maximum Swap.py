class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num2=list(str(num))
        j=len(num2)-1
        if j==0:
            return num
        start=int(num2[-1])
        j-=1
        index=-1
        index0=-1
        while j>=0:
            if int(num2[j])>=start:
                start2=int(num2[j])
                index2=j
                while j>0 and int(num2[j-1])>=int(num2[j]):
                    if int(num2[j-1])>int(num2[j]):
                        start2=int(num2[j-1])
                        index2=j-1
                    j-=1
                if j!=0 and start2>start:
                    start=start2
                    index=index2
                j-=1
            else:
                index0=j
                j-=1
        if index0!=-1:
            num2[index0],num2[index]=num2[index],num2[index0]
            return int(''.join(num2))
        return num
        
num=10909091
c=Solution().maximumSwap(num)

