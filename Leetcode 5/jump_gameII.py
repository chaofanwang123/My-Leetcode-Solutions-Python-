def jump(A):    
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret

A=[2,2,1,1,4]
c=jump(A)
