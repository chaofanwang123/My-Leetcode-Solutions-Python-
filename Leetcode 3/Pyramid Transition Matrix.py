from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def dfs(string):
            n=len(string)
            if n==1:
                return True
            if n>=2:
                for i in range(len(string)-1):
                    if string[i:i+2] not in d:
                        return False
                dp=['']
                for i in range(len(string)-1):
                    temp=[l+r for l in dp for r in d[string[i:i+2]]]
                    dp=temp
                for string2 in dp:
                    if dfs(string2):
                        return True
                return False
                
                
        if allowed==[]:
            return False
        d=defaultdict(list)
        for i in allowed:
            d[i[0:2]].append(i[2])
        return dfs(bottom)            
            
class Solution2:
    def pyramidTransition2(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def allstrings(string):
            n=len(string)
            if n>=2:
                for i in range(len(string)-1):
                    if string[i:i+2] not in d:
                        return []
                dp=['']
                for i in range(len(string)-1):
                    temp=[l+r for l in dp for r in d[string[i:i+2]]]
                    dp=temp
                return dp
            else:
                return []
            
        stack=[bottom]
        if allowed==[]:
            return False
        d=defaultdict(list)
        for i in allowed:
            d[i[0:2]].append(i[2])
        while stack!=[]:
            string=stack.pop(0)
            if len(string)==1:
                return True
            stack+=allstrings(string)
        return False

bottom = "BDBBAA"
allowed = ["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]
c=Solution().pyramidTransition(bottom,allowed)