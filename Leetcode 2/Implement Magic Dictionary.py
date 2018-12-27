class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d=set()
        self.length=set()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.d=set(dict)
        for item in self.d:
            self.length.add(len(item))
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n=len(word)
        if n>=1 and n in self.length:
            for i in range(n):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    if letter!=word[i]:
                        newword=word[:i]+letter+word[i+1:]
                        if newword in self.d:
                            return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

