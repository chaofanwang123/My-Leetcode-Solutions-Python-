class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        i=len(source)-1
        while i>=0:
            if '//' in source[i]:
                index=source[i].find('//')
                source[i]=source[i][:index]
                if source[i]=='':
                    del source[i]
            i-=1
        i=len(source)-1
        while i>=0:
#            if '//' in source[i]:
#                index=source[i].find('//')
#                source[i]=source[i][:index]
#                if source[i]=='':
#                    del source[i]
            if '*/' in source[i]:
                index=source[i].rfind('*/')
                if index>=1 and source[i][index-1]=='/':
                    continue
                rem2=source[i][index+2:]
                j=i
                while j>=0:
                    if '/*' in source[j]:
                        index=source[j].find('/*')
                        if not (index>=1 and source[j][index-1]=='/'):
                            break
                    j-=1
                if j>=0:
                    rem1=source[j][:index]
                    source[j+1:i+1]=[]
                    source[j]=rem1+rem2
                    if source[j]=='':
                        del source[j]
                i=j
            i-=1
        return source
class Solution2(object):
    def removeComments2(self, source):
        # if the comment starts with // we just substringfy everything and attach that to a list
        # if the comment starts with /* we need to add the string until the end
        
        return_list = []
        block_on = False
        cur_string = ""
        for source_string in source:
            index = 0
            while index < len(source_string):
                if block_on:
                    if source_string[index] == "*":
                        if index < len(source_string) - 1 and source_string[index+1] == "/":
                            block_on=False
                            index += 1
                    else:
                        pass
                    
                elif source_string[index] == "/":
                    if index < (len(source_string) - 1) and source_string[index+1] == "*":
                        block_on = True
                        index += 1
                    elif index < (len(source_string) - 1) and source_string[index+1] == "/":
                        break
                    else:
                        cur_string += source_string[index]
                else:
                    cur_string += source_string[index]
                index += 1
            if cur_string != "" and block_on == False:
                return_list.append(cur_string)
                cur_string = ""
        return return_list                
source=["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
c=Solution().removeComments(source)
