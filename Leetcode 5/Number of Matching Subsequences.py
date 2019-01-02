from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def binarysearch(arr,left,right,target):
            if left>right or arr[right]<=target:
                return -1
            if arr[left]>target:
                return left
            while left<right:
                mid=(left+right)//2
                if arr[mid]<target:
                    left=mid+1
                else:
                    right=mid
            return right
        d=defaultdict(list)
        for i in range(len(S)):
            d[S[i]].append(i)
        string='abcdefghijklmnopqrstuvwxyz'
        count=0
        for word in words:
            d2={letter:0 for letter in string}
            if word[0] in d:
                index=d[word[0]][0]
                d2[word[0]]+=1
                note=0                   
                for i in range(1,len(word)):
                    if word[i] in d:
                        j=binarysearch(d[word[i]],d2[word[i]],len(d[word[i]])-1,index)
                        if j==-1:
                            note=1
                            break
                        index=d[word[i]][j]
                        d2[word[i]]=j+1
                    else:
                        note=1
                        break
                if note==0:
                    count+=1
        return count
import bisect
class Solution2:
    def numMatchingSubseq2(self, S, words):
        def isMatch(word, w_i, d_i):
            if w_i == len(word): return True
            l = dict_idxs[word[w_i]]
            if len(l) == 0 or d_i > l[-1]: return False
            i = l[bisect.bisect_left(l, d_i)]
            return isMatch(word, w_i + 1, i + 1)

        dict_idxs = defaultdict(list)
        for i in range(len(S)):
            dict_idxs[S[i]].append(i)
        return sum(isMatch(word, 0, 0) for word in words)
    
class Solution3:
    def numMatchingSubseq3(self, S, words):
        count = 0
        dic = {}
        for word in words:
            if word in dic:  
                count += dic[word]
                continue
            idx = -1
            flag = 0
            for ch in word:
                idx = S.find(ch, idx+1) 
                if idx == -1:
                    flag = 1
                    break
            if flag == 0:
                count += 1
                dic[word] = 1
            else:
                dic[word] = 0
        return count
S = "abcde"
words = ["a", "bb", "acd", "ace"]
c=Solution().numMatchingSubseq(S,words)
