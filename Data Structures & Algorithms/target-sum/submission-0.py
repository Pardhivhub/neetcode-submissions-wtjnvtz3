class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,target):
            if i==len(nums):
                if target==0:
                    return 1
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            add=dfs(i+1,target-nums[i])
            subtract=dfs(i+1,target+nums[i])
            memo[(i,target)]= add+subtract
            return memo[(i,target)]
        return dfs(0,target)
           

        