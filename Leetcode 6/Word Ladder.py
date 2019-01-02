class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        pastset=set()
        pastset.add(beginWord)
        stack=[beginWord]
        count=1
        letters='abcdefghijklmnopqrstuvwxyz'
        m=len(beginWord)
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                word=stack.pop(0)
                for i in range(m):
                    for letter in letters:
                        temp=word[:i]+letter+word[i+1:]
                        if temp==endWord:
                            return count
                        if letter!=word[i] and temp in wordset and temp not in pastset:
                            pastset.add(temp)
                            stack.append(temp)
        return 0
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

c=Solution().ladderLength(beginWord,endWord,wordList)        

