from collections import defaultdict
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not set(s2) <= set(s1):
            return 0
        l1, l2 = len(s1), len(s2)
        dp = defaultdict(dict)
        x1 = x2 = 0
        while x1 < l1 * n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break
            y1, y2 = x1 % l1, x2 % l2
            if y2 not in dp[y1]:
                dp[y1][y2] = x1, x2
            else:
                dx1, dx2 = dp[y1][y2]
                round = (l1 * n1 - dx1) // (x1 - dx1)
                x1 = dx1 + round * (x1 - dx1)
                x2 = dx2 + round * (x2 - dx2)
            if x1 < l1 * n1:
                x1 += 1
                x2 += 1
        return x2 //(n2 * l2)

class Solution2:
    def getMaxRepetitions2(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        indexes = [0] * (len(s2) + 1)       # because of Pigeonhole principle, there will be a pattern
        counts = [0] * (len(s2) + 1)
        
        index = count = 0       # index of char to find in s2
        for i in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[index]:
                    index += 1
                if index == len(s2):
                    index = 0
                    count += 1
            indexes[i] = index      # update variables for this block
            counts[i] = count
            for k in range(i):      # find whether a repeated pattern exists
                if indexes[k] == index:
                    prev_cnt = counts[k]
                    ptrn_cnt = (count - counts[k]) * ((n1 - (k + 1)) // (i - k))  # count from patterns
                    rest_cnt = counts[k + (n1 - (k + 1)) % (i - k)] - counts[k]
                    return (prev_cnt + ptrn_cnt + rest_cnt) // n2
        
        return count // n2      # n1 is too small, no pattern found