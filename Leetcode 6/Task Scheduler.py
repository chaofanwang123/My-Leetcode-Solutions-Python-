class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """            
        d={}
        for i in tasks:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d1=list(d.values())
        m=max(d1)
        count=0
        for i in d1:
            if i==m:
                count+=1
        
        return max(len(tasks),(m-1)*(n+1)+count)
        
#class Solution2:
#    def leastInterval2(self, tasks, n):
#        """
#        :type tasks: List[str]
#        :type n: int
#        :rtype: int
#        """
#        cnt = collections.Counter(tasks)
#        tmax = max(cnt.values())
#        slots = (tmax - 1) * n
#        tsum = len(tasks)
#        temp=sum(n - (n == tmax) for n in cnt.values())
#        return tsum + max(0, slots + tmax - 1 - temp)
                
        
tasks = ["A","A","A","B","B","B","C","C","D"]
n = 2
c=Solution().leastInterval(tasks,n)