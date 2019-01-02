class Solution:
    def validIPAddress(self,IP):
        if '.' in IP:
            vset=set('0123456789')
            List=IP.split('.')
            if len(List)!=4:
                return 'Neither'
            for word in List:
                if not word or len(word)>3:
                    return 'Neither'
                if word[0]=='0':
                    if len(word)>1:
                        return 'Neither'
                else:
                    if not set(word)<vset or int(word)>=256:
                        return 'Neither'
            return 'IPv4'
        if ':' in IP:
            vset=set('0123456789abcdefABCDEF')
            List=IP.split(':')
            if len(List)!=8:
                return 'Neither'
            for word in List:
                if not word or len(word)>4 or not set(word)<vset:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'

IP="20EE:Fb8:85a3:0:0:8A2E:0370:7334"#'2001:0db8:85a3:0000:0:8A2E:0370:7334'
c=Solution().validIPAddress(IP)
        
                    
                
    

