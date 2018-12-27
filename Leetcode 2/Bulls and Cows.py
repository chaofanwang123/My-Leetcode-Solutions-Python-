from collections import defaultdict
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret or not guess:
            return '0A0B'
        countA=0
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                countA+=1
            else:
                d1[secret[i]]+=1
                d2[guess[i]]+=1
        countB=0
        for letter in d2:
            if letter in d1:
                countB+=min(d1[letter],d2[letter])
        return str(countA)+'A'+str(countB)+'B'                

