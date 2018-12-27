class Solution:
    def detectCapitalUse(self,word):
        if not word:
            return True
        set1=set('abcdefghijklmnopqrstuvwxyz')
        set2=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if word[0] in set2:
            return set(word[1:])<=set1 or set(word[1:])<=set2
        elif word[0] in set1:
            return set(word[1:])<=set1
        return False

