class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        vset=set(dict)
        List=sentence.split()
        for i in range(len(List)):
            for j in range(len(List[i])):
                if List[i][:j+1] in vset:
                    List[i]=List[i][:j+1]
                    break
        return ' '.join(List)
        
        

