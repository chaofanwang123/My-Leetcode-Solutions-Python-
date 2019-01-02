class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(string,List,d):
            if string in d and d[string]!=[]:
                d[string].sort()
                airport=d[string].pop(0)
                List.append(airport)
                dfs(airport,List,d)
        d=dict()
        if tickets==[]:
            return []
        n=len(tickets)
        for i in range(n):
            if tickets[i][0] in d:
                d[tickets[i][0]].append(tickets[i][1])
            else:
                d[tickets[i][0]]=[tickets[i][1]]
        List=['JFK']
        dfs('JFK',List,d)
        return List
    
    def findItinerary2(self, tickets):
        d=dict()
        for a, b in sorted(tickets)[::-1]:
            if a in d:
                d[a].append(b)
            else:
                d[a]=[b]
        route = []
        def visit(airport):
            while airport in d and d[airport]!=[]:
                visit(d[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


tickets  = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

c=Solution().findItinerary2(tickets)