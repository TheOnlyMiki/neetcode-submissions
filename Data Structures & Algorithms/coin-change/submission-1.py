class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        count = 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            record = []

            for coin in coins:
                if i >= coin:
                    record.append(dp[i-coin])

            if record:
                dp[i] = min(record) + 1


        return dp[amount] if dp[amount] < float('inf') else -1
