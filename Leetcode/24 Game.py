class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums):
            n=len(nums)
            if n==2:
                error=1e-9
                if abs((nums[0]+nums[1])-24)<error or abs(abs(nums[0]-nums[1])-24)<error or abs(nums[0]*nums[1]-24)<error:
                    return True
                if (nums[1]!=0 and abs(nums[0]/nums[1]-24)<error) or (nums[0]!=0 and abs(nums[1]/nums[0]-24)<error):
                    return True
            if n==3:
                List=[[nums[0],nums[1],nums[2]],[nums[1],nums[0],nums[2]],[nums[2],nums[0],nums[1]]]
                for x,y,z in List:
                    if dfs([x]+[y+z]) or dfs([x]+[y-z]) or dfs([x]+[z-y]) or dfs([x]+[y*z]) or (z!=0 and dfs([x]+[y/z])) or (y!=0 and dfs([x]+[z/y])):
                        return True
                return False
            if n==4:
                List=[[[nums[0],nums[1]],nums[2],nums[3]],[[nums[0],nums[2]],nums[1],nums[3]],[[nums[0],nums[3]],nums[1],nums[2]]]
                List.append([[nums[1],nums[2]],nums[0],nums[3]])
                List.append([[nums[1],nums[3]],nums[0],nums[2]])
                List.append([[nums[2],nums[3]],nums[0],nums[1]])
                for x,y,z in List:
                    if dfs(x+[y+z]) or dfs(x+[y-z]) or dfs(x+[z-y]) or dfs(x+[y*z]) or (z!=0 and dfs(x+[y/z])) or (y!=0 and dfs(x+[z/y])):
                        return True
                return False
        return dfs(nums)
            
class Solution_2:
    def judgePoint24_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def twonums(nums,target):
            if nums[1]-nums[0]==target or nums[1]+nums[0]==target:
                return True
            if nums[1]*nums[0]==target or nums[1]/nums[0]==target:
                return True
            return False
        def threenums(nums,target):
            if target>=48:
                if target%nums[0] and twonums(nums[1:],target//nums[0]):
                    return True
                if target%nums[1] and twonums([nums[0]]+[nums[2]],target//nums[1]):
                    return True
                if target%nums[2] and twonums(nums[:2],target//nums[2]):
                    return True
                if twonums(nums[1:],target+nums[0]) or twonums(nums[1:],target-nums[0]):
                    return True
                if twonums([nums[0]]+[nums[2]],target+nums[1]) or twonums([nums[0]]+[nums[2]],target-nums[1]):
                    return True
                if twonums(nums[:2],target+nums[2]) or twonums(nums[:2],target-nums[2]):
                    return True
                return False
                
            # 2*1
            if (nums[1]-nums[0])*nums[2]==target or (nums[1]+nums[0])*nums[2]==target:
                return True
            if (nums[1]-nums[0])/nums[2]==1/target or (nums[1]+nums[0])/nums[2]==1/target:
                return True
            if (nums[2]-nums[0])*nums[1]==target or (nums[2]+nums[0])*nums[1]==target:
                return True
            if (nums[2]-nums[0])/nums[1]==target or (nums[2]+nums[0])/nums[1]==target:
                return True
            if (nums[2]-nums[0])/nums[1]==1/target:
                return True
            if (nums[2]-nums[1])*nums[0]==target or (nums[2]+nums[1])*nums[0]==target:
                return True
            if (nums[2]-nums[1])/nums[0]==target or (nums[2]+nums[1])/nums[0]==target:
                return True
            if (nums[2]-nums[1])/nums[0]==1/target:
                return True
            # 3
            if twonums(nums[:2],abs(target-nums[2])) or twonums(nums[:2],target+nums[2]):
                return True
            if twonums([nums[0]]+[nums[2]],abs(target-nums[1])) or twonums([nums[0]]+[nums[2]],target+nums[1]):
                return True
            if twonums(nums[1:],abs(target-nums[0])) or twonums(nums[1:],target+nums[0]):
                return True
            return False
            
        nums.sort()
        # check 3 * 1
        for i in range(4):
            if 24%nums[i]==0 and threenums(nums[:i]+nums[i+1:],24//nums[i]):
                return True
            if threenums(nums[:i]+nums[i+1:],24*nums[i]):
                return True 
        # check 2*2
        List=[[nums[0],nums[1],nums[2],nums[3]],[nums[0],nums[2],nums[1],nums[3]],[nums[0],nums[3],nums[1],nums[2]]]
        for x1,x2,x3,x4 in List:
            if (x1+x2)*(x3+x4)==24 or (x2-x1)*(x4-x3)==24 or (x1+x2)*(x4-x3)==24 or (x2-x1)*(x3+x4)==24:
                return True
        # check 2*1+1
        for i in range(4):
            if threenums(nums[:i]+nums[i+1:],24-nums[i]) or threenums(nums[:i]+nums[i+1:],24+nums[i]):
                return True
        # check (1*1)+(1*1)
        for x1,x2,x3,x4 in List:
            if (x1*x2+x3*x4)==24 or abs(x1*x2-x3*x4)==24:
                return True
            if (x1*x2+x4/x3)==24 or (x2/x1+x4*x3)==24 or (x1*x2-x4/x3)==24 or (x3*x4-x2/x1)==24:
                return True 
        return False

nums=[3,3,8,8]
c=Solution().judgePoint24(nums)
        
        
                
                
        

