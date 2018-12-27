class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        step=abs(target[0])+abs(target[1])
        for x,y in ghosts:
            if abs(x-target[0])+abs(y-target[1])<=step:
                return False
        return True

