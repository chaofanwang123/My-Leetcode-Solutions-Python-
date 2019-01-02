class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        distance=1
        i=0
        n=len(seats)
        while i<n and seats[i]==0:
            i+=1
        distance=max(distance,i)
        while i<n:
            j=i+1
            while j<n and seats[j]==0:
                j+=1
            if j<n:
                distance=max(distance,(j-i)//2)
            else:
                distance=max(distance,n-1-i)
            i=j
        return distance

