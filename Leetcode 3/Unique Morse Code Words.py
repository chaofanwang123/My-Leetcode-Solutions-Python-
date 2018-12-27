class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
               "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        for i,letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            d[letter]=morse[i]
        vset=set()
        for word in words:
            temp=''
            for letter in word:
                temp+=d[letter]
            vset.add(temp)
        return len(vset)
            