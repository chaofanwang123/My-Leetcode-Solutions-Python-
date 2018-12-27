from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def dfs(u,List):
            visited[u]=True
            for mail in accounts[u][1:]:
                List.add(mail)
                for item in d[mail]:
                    if not visited[item]:
                        dfs(item,List)
            
        d=defaultdict(list)
        n=len(accounts)
        for i in range(n):
            for mail in accounts[i][1:]:
                d[mail].append(i)
        
        
        visited=[False for i in range(n)]
        ans=[]
        for i in range(n):
            if visited[i]==False:
                List=set([])
                dfs(i,List)
                ans.append([accounts[i][0]]+sorted(List))
        return ans
        
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
c=Solution().accountsMerge(accounts)    

