class Solution:
    def maxProduct(self,nums):
        n=len(nums)
        if n==1:
            return nums[0]
        max_negative=1
        max_value=0
        product=1
        for i in range(n):
            if nums[i]==0:
                max_negative=1
                product=1
            else:
                product=product*nums[i]
                if product>0:
                    max_value=max(max_value,product)
                elif max_negative<0:
                    max_value=max(max_value,product/max_negative)
                else:
                    max_negative=product
        return max_value

