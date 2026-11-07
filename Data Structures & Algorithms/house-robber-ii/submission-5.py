from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # One-house edge case
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr: List[int]) -> int:
            # Bottom-up DP for houses arranged in a straight line
            n = len(arr)

            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            # dp[i] = maximum loot from houses 0 through i
            dp = [0] * n

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                skip_current_house = dp[i - 1]
                rob_current_house = dp[i - 2] + arr[i]

                dp[i] = max(skip_current_house, rob_current_house)

            return dp[n - 1]

        # Circular rule: first and last houses cannot both be robbed.
        exclude_first = rob_line(nums[1:])
        exclude_last = rob_line(nums[:-1])

        return max(exclude_first, exclude_last)