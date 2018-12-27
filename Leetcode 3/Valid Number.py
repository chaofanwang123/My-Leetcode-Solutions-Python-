class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def number(x):
            if x=='0' or x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9':
                return 1
            else:
                return -1
        def check_space(s,index):
            if index==len(s):
                return 1
            while s[index]==' ':
                index+=1
                if index==len(s):
                    return 1
            return -1
        # check + and -
        def check_minus_plus(s,index):
            if index<len(s) and number(s[index])==1:
                while number(s[index])==1:
                    index+=1
                    if index==len(s):
                        return 1
                if s[index]==' ':
                    return check_space(s,index+1)
                return -1
            return -1
        # check if it is numeric after 'e'
        def check_after_e(s,index):
            if index==len(s):
                return -1
            
            if s[index-2]=='.' and ((number(s[index-3])!=1 and index>=3) or index==2):
                return False
            #check + and -
            if s[index]=='-' or s[index]=='+':
                return check_minus_plus(s,index+1)
            if number(s[index])!=1:
                return -1
            while number(s[index])==1:
                index+=1
                if index==len(s):
                    return 1
            if s[index]==' ':
                return check_space(s,index)
            return -1
        # check if it is numeric after '.'
        def check_after_dot(s,index):
            if index==len(s):
                if index>=2 and number(s[index-2])==1:
                    return 1
                return -1
            # space after .
            if s[index]==' ':
                if number(s[index-2])==1 and check_space(s,index+1)==1:
                    return 1
                return -1                
            while number(s[index])==1:
                index+=1
                if index==len(s):
                    return 1
            if s[index]==' ':
                return check_space(s,index+1)
            if s[index]=='e':      
                return check_after_e(s,index+1)
            return -1
            
        i=0
        while s[i]==" ":
            i+=1
            if i==len(s):
                return False
        # check if is '-' or '+'
        if s[i]=='-' or s[i]=='+':
            i+=1
            if i==len(s):
                return False
            if s[i]=='.':
                return check_after_dot(s,i+1)==1
            if number(s[i])==1:
                i+=1
                if i==len(s):
                    return True
                while number(s[i])==1:
                    i+=1
                    if i==len(s):
                        return True
                if s[i]=='.':
                    return check_after_dot(s,i+1)==1
                if s[i]==' ':
                    return check_space(s,i+1)==1
                if s[i]=='e':
                    return check_after_e(s,i+1)==1
                return False
            return False
                
        # check if the first is '.'
        if s[i]=='.':
            i+=1
            if i==len(s):
                return False
            if check_after_dot(s,i)==1:
                return True
            return False            
        elif number(s[i])==1:
            while number(s[i])==1:
                i+=1
                if i==len(s):
                    return True
            if s[i]=='.':
                if check_after_dot(s,i+1)==1:
                    return True
                return False
            elif s[i]=='e':
                if check_after_e(s,i+1)==1:
                    return True
                return False
            elif s[i]==' ':
                if check_space(s,i+1)==1:
                    return True
                return False
            return False
        else:
            return False
