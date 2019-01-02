class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordlist=set(wordList)    
        if endWord not in wordlist:
            return []
        k=len(beginWord)
        ans=[]
        stack=[]        
        
        letterlist='abcdefghijklmnopqrstuvwxyz'
        for letter in letterlist:
            for i in range(k):
                if letter!=beginWord[i]:
                    newword=beginWord[:i]+letter+beginWord[i+1:]
                    if newword==endWord:
                        return [[beginWord,endWord]]
                    if newword in wordlist:
                        stack.append([newword])
        note=0
        while stack and note==0:
            for i in range(len(stack)):
                wordlist.discard(stack[i][-1])
            while i>=0:
                i-=1
                stacklist=stack.pop(0)
                for letter in letterlist:
                    for j in range(k):
                        if letter!=stacklist[-1][j]:
                            newword=stacklist[-1][:j]+letter+stacklist[-1][j+1:]
                            if newword==endWord:
                                ans.append([beginWord]+stacklist+[endWord])
                                note=1
                                break
                            if newword in wordlist:
                                stack.append(stacklist+[newword])
        return ans
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
c=Solution().findLadders(beginWord,endWord,wordList)
        



