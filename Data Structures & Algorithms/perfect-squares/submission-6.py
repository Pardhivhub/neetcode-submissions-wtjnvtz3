class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = minimum perfect squares needed to make i
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for total in range(1, n + 1):
            for num in range(1, int(total ** 0.5) + 1):
                square = num * num

                dp[total] = min(
                    dp[total],
                    1 + dp[total - square]
                )

        return dp[n]