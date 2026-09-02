class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dfs(arr,i,dp):
            if i >=len(arr):
                return 0
            if i in dp:
                return dp[i]
            take=arr[i]+dfs(arr,i+2,dp)
            skip=dfs(arr,i+1,dp)
            dp[i]=max(take,skip)
            return dp[i]
        case1=dfs(nums[1:],0,{})
        case2=dfs(nums[:-1],0,{})
        return max(case1, case2)
        