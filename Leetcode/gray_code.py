class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        arr=[0,1]
        for i in range(1,n):
            m=len(arr)
            temp=arr[m-1::-1]
            for j in range(m):
                temp[j]=temp[j]+pow(2,i)
            arr=arr+temp
        return arr

c=Solution().grayCode(2)

