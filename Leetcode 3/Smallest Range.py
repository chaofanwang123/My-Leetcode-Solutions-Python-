import bisect
class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n=len(nums)
        small_list=[[nums[i][0],i] for i in range(n)]
        large_list=[[nums[i][-1],i] for i in range(n)]
        small_list.sort(key=lambda x:x[0])
        large_list.sort(key=lambda x:x[0])
        smallvalue=[small_list[i][0] for i in range(n)]
        smallindex=[small_list[i][1] for i in range(n)]
        largevalue=[large_list[i][0] for i in range(n)]
        largeindex=[large_list[i][1] for i in range(n)]
        
        while True:
            dif1,dif2=smallvalue[-1]-smallvalue[0],largevalue[-1]-largevalue[0]
            if dif1>dif2:
                popindex=smallindex.pop(0)
                smallvalue.pop(0)
                nums[popindex].pop(0)
                insertindex=bisect.bisect(smallvalue,nums[popindex][0])
                smallvalue.insert(insertindex,nums[popindex][0])
                smallindex.insert(insertindex,popindex)
            elif dif2>dif1:
                popindex=largeindex.pop()
                largevalue.pop()
                nums[popindex].pop()
                insertindex=bisect.bisect(largevalue,nums[popindex][-1])
                largevalue.insert(insertindex,nums[popindex][-1])
                largeindex.insert(insertindex,popindex)
            else:
                popindex=largeindex.pop()
                if len(nums[popindex])==1:
                    return [smallvalue[0],smallvalue[-1]]
                largevalue.pop()
                nums[popindex].pop()
                insertindex=bisect.bisect(largevalue,nums[popindex][-1])
                largevalue.insert(insertindex,nums[popindex][-1])
                largeindex.insert(insertindex,popindex)

nums=[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
c=Solution().smallestRange(nums)
            
                
