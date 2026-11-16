class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(coin_i, total):
            if total == amount:
                return 1

            if coin_i >= len(coins) or total > amount:
                return 0

            if (coin_i, total) in dp:
                return dp[(coin_i, total)]

            dp[(coin_i, total)] = dfs(coin_i, total + coins[coin_i])

            dp[(coin_i, total)] += dfs(coin_i+1, total)

            return dp[(coin_i, total)]

        return dfs(0, 0)

        dp = {}

        def dfs(i, total):
            if i == len(coins) or total > amount:
                return 0

            if total == amount:
                return 1

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i, total + coins[i]) + dfs(i+1, total)

            return dp[(i, total)]

        return dfs(0, 0)



        
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] += dp[i-coin]

        return dp[amount]