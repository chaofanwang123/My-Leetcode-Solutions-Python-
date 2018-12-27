class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        List1,List2=version1.split('.'),version2.split('.')
        while List1 and List2:
            p1,p2=int(List1.pop(0)),int(List2.pop(0))
            if p1>p2:
                return 1
            elif p1<p2:
                return -1
        if List1:
            for i in range(len(List1)):
                if int(List1[i])!=0:
                    return 1
            return 0
        if List2:
            for i in range(len(List2)):
                if int(List2[i])!=0:
                    return -1
            return 0
        return 0
            
version1 = "1.0"
version2 = "1"
c=Solution().compareVersion(version1,version2)