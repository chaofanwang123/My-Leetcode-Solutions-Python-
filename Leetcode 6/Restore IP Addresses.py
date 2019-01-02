class Solution:
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ip):
            if sub == 4:                                        
                if s == '':
                    ans.append(ip[1:])                          
                return
            for i in range(1, 4):                               
                if i <= len(s):                                 
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub+1, ip+'.'+s[:i])
                    if s[0] == '0': break                       
        ans = []
        dfs(s, 0, '')
        return ans

