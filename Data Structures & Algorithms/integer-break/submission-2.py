class Solution:
    def integerBreak(self, n: int) -> int:
        memo={}
        def dfs(rem):
            if rem==1:
                return 1
            if rem in memo:
                return memo[rem]
            best=0
            for i in range(1,rem):
                second=rem-i
                stop=second*i
                split=i*dfs(second)
                best=max(best,split,stop)
            memo[rem]=best
            return best
        return dfs(n)

                
        