class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d=dict()
        for letter in ransomNote:
            if letter not in d:
                d[letter]=1
            else:
                d[letter]+=1
        for letter in d:
            if magazine.count(letter)<d[letter]:
                return False
        return True
        

