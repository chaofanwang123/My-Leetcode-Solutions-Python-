from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d=defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.d[len(word)].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) in self.d:
            if '.' not in word:
                return word in self.d[len(word)]
            else:
                for item in self.d[len(word)]:
                    i=0
                    note=0
                    while i<len(word):
                        if word[i]!='.' and word[i]!=item[i]:
                            note=1
                            break
                        i+=1
                    if note==0:
                        return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('a')
obj.addWord('ab')
param_2 = obj.search('.a')

