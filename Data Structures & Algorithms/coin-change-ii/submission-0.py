class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        memo={}
        def dfs(i,target):
            if i>=len(coins):
                return 0
            if target==0:
                return 1
            if (i,target) in memo:
                return memo[(i,target)]
            if target>=coins[i]:
                take=dfs(i,target-coins[i])
                not_take=dfs(i+1,target)
                memo[(i,target)]=take + not_take
            else:
                memo[(i,target)]=dfs(i+1,target)
            return memo[(i,target)]
        return dfs(0,target)
            

            
            
            
        