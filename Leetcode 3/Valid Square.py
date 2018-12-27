class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        x1,y1=p1[0],p1[1]
        x2,y2=p2[0],p2[1]
        x3,y3=p3[0],p3[1]
        x4,y4=p4[0],p4[1]
        l1=(x2-x1)**2+(y2-y1)**2
        l2=(x3-x2)**2+(y3-y2)**2
        l3=(x4-x3)**2+(y4-y3)**2
        l4=(x1-x4)**2+(y1-y4)**2
        l13=(x3-x1)**2+(y3-y1)**2
        l24=(x4-x2)**2+(y4-y2)**2
        l14=(x4-x1)**2+(y4-y1)**2
        l23=(x3-x2)**2+(y3-y2)**2
        if l1!=0 and l1==l2==l3==l4 and l13==l24==2*l1:
            return True
        elif l1!=0 and l1==l3==l13==l24 and l14==l23==2*l1:
            return True
        elif l4!=0 and l13==l24==l2==l4 and l1==l3==2*l2:
            return True
        return False
            
                    
p1=[0,0]
p2=[1,1]
p3=[1,0]
p4=[0,1]
c=Solution().validSquare(p1,p2,p3,p4)
