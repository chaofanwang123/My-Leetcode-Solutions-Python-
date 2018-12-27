from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
        for path in paths:
            s=path.split()
            root=s.pop(0)
            for file in s:
                start,end=file.index('('),file.index(')')
                content=file[start+1:end]
                d[content].append(root+'/'+file[:start])
        return [item for item in d.values() if len(item)>1]
                
paths=["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
c=Solution().findDuplicate(paths)