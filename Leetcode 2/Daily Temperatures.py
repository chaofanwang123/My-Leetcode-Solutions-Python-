class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack=[0]
        ans=[0]*len(T)
        i=1
        while i<len(T):
            if not stack or T[i]<=T[stack[-1]]:
                stack.append(i)
            else:
                while stack and T[i]>T[stack[-1]]:
                    index=stack.pop()
                    ans[index]=i-index
                stack.append(i)
            i+=1
        return ans
        
T=[73,74,75,71,69,72,76,73]
c=Solution().dailyTemperatures(T)       

