def comsum(arr,index,target,link,List):
    if index<0 or target<0:
        return
    if target==0:
        if link not in List:
            List.append(link)
    else:
        if index>0:
            comsum(arr,index-1,target,link,List)
            comsum(arr,index-1,target-arr[index-1],[arr[index-1]]+link,List)
    return
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        index=0
        n=len(candidates)
        while index<n and candidates[index]<=target:
            index+=1
        arr=candidates[:index]
        List=[]
        link=[]
        comsum(arr,index,target,link,List)
        return List
        
candidates = [10,1,2,7,6,1,5]
target = 2
c=Solution().combinationSum2(candidates, target)
            

