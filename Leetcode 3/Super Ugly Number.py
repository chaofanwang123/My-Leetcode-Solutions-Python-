class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        candidates = [1]*len(primes)
        ids = [0]*len(primes)
        superNums = [1]
        nextMin = 1
        for count in range(1, n) :
            for i in range(len(primes)) :
                if nextMin == candidates[i] :
                    candidates[i] = superNums[ids[i]]*primes[i]
                    ids[i] += 1
            nextMin = min(candidates)
            superNums.append(nextMin)
        return superNums[-1]

n = 12
primes = [2,3,5,7]
c=Solution().nthSuperUglyNumber(n,primes)