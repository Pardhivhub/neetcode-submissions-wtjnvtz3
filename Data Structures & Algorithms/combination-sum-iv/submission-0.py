class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(left):
            if left ==0:
                return 1
            if left<0:
                return 0
            if left in memo:
                return memo[left]
            comb=0
            for num in nums:
                comb+=dfs(left-num)
            
            memo[left]=comb
            return comb
        return dfs(target)