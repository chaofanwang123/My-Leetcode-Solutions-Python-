class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        if not equation:
            return 'Infinite solutions'
        i=len(equation)-1
        equation=list(equation)
        while i>=0:
            if equation[i]=='-':
                equation.insert(i,'+')
            i-=1
        equation=''.join(equation)
        index=equation.find('=')
        List1,List2=equation[:index].split('+'),equation[index+1:].split('+')
        if List1[0]=='':
            del List1[0]
        if List2[0]=='':
            del List2[0]
        coef1,const1=0,0
        for word in List1:
            sign=1
            if word[0]=='-':
                sign=-1
                word=word[1:]
            if word[-1]=='x':
                if word=='x' or word=='-x':
                    coef1+=sign
                else:
                    coef1+=sign*int(word[:-1])
            else:
                const1+=sign*int(word)
        
        coef2,const2=0,0
        for word in List2:
            sign=1
            if word[0]=='-':
                sign=-1
                word=word[1:]
            if word[-1]=='x':
                if word=='x' or word=='-x':
                    coef2+=sign
                else:
                    coef2+=sign*int(word[:-1])
            else:
                const2+=sign*int(word)
        
        coef,const=coef1-coef2,const2-const1
        if coef==0:
            return 'Infinite solutions' if const==0 else 'No solution'
        return 'x='+str(const//coef)

equation="-x=-1"
c=Solution().solveEquation(equation)