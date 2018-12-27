class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            res.append(dict[item])
        return res

strs=["eat", "tea", "tan", "ate", "nat", "bat"]
c=Solution().groupAnagrams(strs)