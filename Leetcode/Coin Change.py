import bisect
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        if not coins:
            return -1
        stack=[amount]
        coins.sort()
        count=0
        vset=set()
        while stack:
            n=len(stack)
            count+=1
            while n>0:
                n-=1
                p=stack.pop(0)
                if p>=coins[0]:
                    index=bisect.bisect_right(coins,p)
                    for i in range(index):
                        temp=p-coins[i]
                        if temp==0:
                            return count
                        if temp not in vset:
                            vset.add(temp)
                            stack.append(temp)
        return -1
                  
coins = [2,1,5]
amount = 31
c=Solution().coinChange(coins,amount)