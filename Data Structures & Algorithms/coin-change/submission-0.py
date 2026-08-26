class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def f(i,amount):
            if amount==0:
                return 0
            if i<0:
                return float("inf")
            if (i,amount) in dp:
                    return dp[(i,amount)]
            if coins[i]<=amount:
                    take=1+f(i,amount-coins[i])
                    not_take=f(i-1,amount)
                    dp[(i,amount)]=min(take,not_take)
            else:
                    dp[(i,amount)]=f(i-1,amount)
            return dp[(i,amount)]
        answer=f(len(coins)-1,amount)
        if answer==float("inf"):
            return -1
        return answer

                