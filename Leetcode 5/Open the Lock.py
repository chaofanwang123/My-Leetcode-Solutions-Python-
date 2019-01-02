class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target=='0000':
            return 0
        stack=['0000']
        deadset=set(deadends)
        if '0000' in deadset:
            return -1
        deadset.add('0000')
        count=0
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                p=stack.pop(0)
                for i in range(4):
                    newstring1=p[:i]+str((int(p[i])+1)%10)+p[i+1:]
                    newstring2=p[:i]+str((int(p[i])-1)%10)+p[i+1:]
                    if newstring1==target or newstring2==target:
                        return count
                    if newstring1 not in deadset:
                        deadset.add(newstring1)
                        stack.append(newstring1)
                    if newstring2 not in deadset:
                        deadset.add(newstring2)
                        stack.append(newstring2)
        return -1
                
deadends = ['0000']
target = "8888"
c=Solution().openLock(deadends,target)