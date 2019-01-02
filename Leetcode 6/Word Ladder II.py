class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def buildPath(path,word):
            if word==beginWord:
                result.append([word] + path)
                return
            path.insert(0,word)
            for w in preMap[word]:
                buildPath(path,w)
            path.pop(0)

        length = len(beginWord)
        wordlist=set(wordList)
        preMap = {}
        for word in wordlist:
            preMap[word] = []
        result = []
        cur_level = set()
        cur_level.add(beginWord)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level: 
                wordlist.discard(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in wordlist:
                                preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:
                return []
            if endWord in cur_level:
                break
        buildPath([],endWord)
        return result
from collections import defaultdict

class Solution2(object):
    def findLadders2(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        word_dict = set(wordList)
        front, back = set([beginWord]), set([endWord])
        direct = 1
        parents = defaultdict(set)
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                direct *= -1
            next_layer = set()
            word_dict -= front
            for word in front:
                for i in range(len(beginWord)):
                    prefix, postfix = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = prefix + c + postfix
                        if new_word in word_dict:
                            next_layer.add(new_word)
                            if direct == 1:
                                parents[new_word].add(word)
                            else:
                                parents[word].add(new_word)
            if next_layer & back:
                rlt = [[endWord]]
                while rlt[0][0] != beginWord:
                    rlt = [[pa] + r for r in rlt for pa in parents[r[0]]]
                return rlt
            front = next_layer
        return []
    
class Solution3:
    def findLadders3(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def transferable(str1,str2):
            count=0
            for i in range(k):
                if str1[i]!=str2[i]:
                    count+=1
                if count==2:
                    return False
            return True if count==1 else False
            
        if endWord not in wordList:
            return []
        n=len(wordList)
        k=len(beginWord)
        if transferable(endWord,beginWord):
            return [[beginWord,endWord]]
        d=defaultdict(list)

        ans=[]
        for i in range(n-1):
            for j in range(i+1,n):
                if transferable(wordList[i],wordList[j]):
                    d[i].append(j)
                    d[j].append(i)
        stack=[]        
        vset=set([])
        for i in range(n):
            if transferable(beginWord,wordList[i]):
                stack.append([i])
                vset.add(i)
        note=0
        while stack and note==0:
            i=len(stack)-1
            while i>=0:
                i-=1
                stacklist=stack.pop(0)
                vset1=set([])
                if stacklist[-1] in d:
                    for index in d[stacklist[-1]]:
                        if wordList[index]==endWord:
                            temp=[wordList[j] for j in stacklist]
                            ans.append(temp+[endWord])
                            note=1
                            break
                        if index not in vset and wordList[index]!=beginWord:
                             stack.append(stacklist+[index])
                             vset1.add(index)
            vset.update(vset1)
        if ans:
            return [[beginWord]+item for item in ans]
        return ans
    
#beginWord = "cet"
#endWord = "ism"
#wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
c=Solution().findLadders(beginWord,endWord,wordList)
        

