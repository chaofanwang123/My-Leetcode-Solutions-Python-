class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ''
        i=len(expression)-1
        expression=list(expression)
        while i>=0:
            if expression[i]=='-':
                expression.insert(i,'+')
            i-=1
        expression=''.join(expression)
        List=expression.split('+')
        if List[0]=='':
            del List[0]
        nom,dem=0,1
        for word in List:
            sign=1
            if word[0]=='-':
                sign=-1
                word=word[1:]
            index=word.find('/')
            tempnom,tempdem=sign*int(word[:index]),int(word[index+1:])
            nom,dem=tempdem*nom+tempnom*dem,dem*tempdem
            for j in range(min(abs(nom),dem),1,-1):
                if nom%j==0 and dem%j==0:
                    nom//=j
                    dem//=j
                    break
        if nom==0:
            return '0/1'
        return str(nom)+'/'+str(dem)
            
expression="-1/4-4/5-1/4"
c=Solution().fractionAddition(expression)            
                
            

