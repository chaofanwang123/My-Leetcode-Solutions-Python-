class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(nums)
        n=len(nums[0])
        if m*n!=r*c:
            return nums
        matrix2=[[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                index=i*c+j
                i1,j1=index//n,index%n
                matrix2[i][j]=nums[i1][j1]
        return matrix2

nums=[[1,2,3,4]]
c=Solution().matrixReshape(nums,2,2)